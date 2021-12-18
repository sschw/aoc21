// AoC.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <vector>
#include <set>
#include <utility>

using namespace std;

string getFile() {
    ifstream file("day15input.txt");
    return string((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
}

const std::string WHITESPACE = " \n\r\t\f\v";

string ltrim(const std::string& s)
{
    size_t start = s.find_first_not_of(WHITESPACE);
    return (start == std::string::npos) ? "" : s.substr(start);
}

string rtrim(const std::string& s)
{
    size_t end = s.find_last_not_of(WHITESPACE);
    return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}

string trim(const std::string& s) {
    return rtrim(ltrim(s));
}

struct Packet {
    uint8_t version;
    uint8_t type;

    virtual uint64_t getValue() = 0;
    virtual vector<Packet*> getContent() = 0;
};

struct Literal : public Packet {
    uint64_t value;

     uint64_t getValue() override { return value; }
     vector<Packet*> getContent() override { return vector<Packet*>(); }
};

struct Operator : public Packet {
    uint8_t lengthType;
    uint32_t length;
    vector<Packet*> content;

    uint64_t getValue() override { return 0; } // for now.
    vector<Packet*> getContent() override { return content; }
};

struct SumOperator : public Operator {
    uint64_t getValue() override {
        uint64_t sum = 0;
        for (auto& c : content)
            sum += c->getValue();
        return sum;
    }
};

struct ProductOperator : public Operator {
    uint64_t getValue() override {
        uint64_t prod = 0;
        bool first = true;
        for (auto& c : content)
            if (first) {
                prod = c->getValue();
                first = false;
            }
            else
                prod *= c->getValue();
        return prod;
    }
};

struct MinOperator : public Operator {
    uint64_t getValue() override {
        uint64_t min = 0;
        bool first = true;
        for (auto& c : content)
            if (first) {
                min = c->getValue();
                first = false;
            }
            else if (min > c->getValue())
                min = c->getValue();
        return min;
    }
};

struct MaxOperator : public Operator {
    uint64_t getValue() override {
        uint64_t max = 0;
        for (auto& c : content)
            if (max < c->getValue())
                max = c->getValue();
        return max;
    }
};

struct GTOperator : public Operator {
    uint64_t getValue() override {
        return content[0]->getValue() > content[1]->getValue();
    }
};

struct LTOperator : public Operator {
    uint64_t getValue() override {
        return content[0]->getValue() < content[1]->getValue();
    }
};

struct EQOperator : public Operator {
    uint64_t getValue() override {
        return content[0]->getValue() == content[1]->getValue();
    }
};

struct SumVersionOperator : public Operator {
    void countVersion(Packet* p, uint64_t& versions) {
        versions += p->version;
        for (auto& c : p->getContent()) {
            countVersion(c, versions);
        }
    }

    uint64_t getValue() override {
        uint64_t versions = 0;
        countVersion(this, versions);
        return versions;
    }
};

pair<uint8_t, uint8_t> readHeader(const uint8_t* ptr, uint32_t& bitOffset) {
    uint8_t version = 0;
    uint8_t type = 0;
    for (int i = 0; i < 3; i++) {
        version = (version << 1) + (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1);
        bitOffset++;
    }
    for (int i = 0; i < 3; i++) {
        type = (type << 1) + (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1);
        bitOffset++;
    }
    return pair(version, type);
}

uint64_t literalValue(const uint8_t* ptr, uint32_t& bitOffset) {
    uint64_t value = 0;
    bool end = false;
    while (!end) {
        end = (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1) == 0;
        bitOffset++;
        for (int i = 0; i < 4; i++) {
            value = (value << 1) + (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1);
            bitOffset++;
        }
    }
    return value;
}

pair<uint8_t, uint32_t> operatorLength(const uint8_t* ptr, uint32_t& bitOffset) {
    uint8_t lengthType = (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1);
    uint32_t bitsToRead = 11;
    if (lengthType == 0)
        bitsToRead = 15;
    bitOffset++;
    uint32_t value = 0;
    for (int i = 0; i < bitsToRead; i++) {
        value = (value << 1) + (((*(ptr+(bitOffset/8))) >> (7-(bitOffset%8))) & 1);
        bitOffset++;
    }
    return pair(lengthType, value);
}

void operatorValue(Operator* op, const uint8_t* ptr, uint32_t& bitOffset) {
    uint32_t startOffset = bitOffset;
    while (op->lengthType == 0 && bitOffset - startOffset < op->length || op->lengthType == 1 && op->content.size() < op->length) {
        const auto& [v, t] = readHeader(ptr, bitOffset);
        if (t == 4) {
            auto l = new Literal();
            l->version = v;
            l->type = t;
            l->value = literalValue(ptr, bitOffset);
            op->content.push_back(l);
        }
        else if (t == 0) {
            auto o = new SumOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 1) {
            auto o = new ProductOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 2) {
            auto o = new MinOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 3) {
            auto o = new MaxOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 5) {
            auto o = new GTOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 6) {
            auto o = new LTOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else if (t == 7) {
            auto o = new EQOperator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
        else {
            auto o = new Operator();
            o->version = v;
            o->type = t;
            const auto [lengthType, length] = operatorLength(ptr, bitOffset);
            o->lengthType = lengthType;
            o->length = length;
            operatorValue(o, ptr, bitOffset);
            op->content.push_back(o);
        }
    }
}

int main()
{
    //string input = trim(getFile());
    string input = "220D790065B2745FF004672D99A34E5B33439D96CEC80373C0068663101A98C406A5E7395DC1804678BF25A4093BFBDB886CA6E11FDE6D93D16A100325E5597A118F6640600ACF7274E6A5829B00526C167F9C089F15973C4002AA4B22E800FDCFD72B9351359601300424B8C9A00BCBC8EE069802D2D0B945002AB2D7D583E3F00016B05E0E9802BA00B4F29CD4E961491CCB44C6008E80273C393C333F92020134B003530004221347F83A200D47F89913A66FB6620016E24A007853BE5E944297AB64E66D6669FCEA0112AE06009CAA57006A0200EC258FB0440010A8A716A321009DE200D44C8E31F00010887B146188803317A3FC5F30056C0150004321244E88C000874468A91D2291802B25EB875802B28D13550030056C0169FB5B7ECE2C6B2EF3296D6FD5F54858015B8D730BB24E32569049009BF801980803B05A3B41F1007625C1C821256D7C848025DE0040E5016717247E18001BAC37930E9FA6AE3B358B5D4A7A6EA200D4E463EA364EDE9F852FF1B9C8731869300BE684649F6446E584E61DE61CD4021998DB4C334E72B78BA49C126722B4E009C6295F879002093EF32A64C018ECDFAF605989D4BA7B396D9B0C200C9F0017C98C72FD2C8932B7EE0EA6ADB0F1006C8010E89B15A2A90021713610C202004263E46D82AC06498017C6E007901542C04F9A0128880449A8014403AA38014C030B08012C0269A8018E007A801620058003C64009810010722EC8010ECFFF9AAC32373F6583007A48CA587E55367227A40118C2AC004AE79FE77E28C007F4E42500D10096779D728EB1066B57F698C802139708B004A5C5E5C44C01698D490E800B584F09C8049593A6C66C017100721647E8E0200CC6985F11E634EA6008CB207002593785497652008065992443E7872714";
    uint8_t* data = new uint8_t[input.length()/2];
    for (int i = 0; i < input.length()/2; i++) {
        data[i] = 0;
        for (int j = 0; j < 2; j++) {
            data[i] = (data[i] << 4) + (input[i*2+j] < 'A' ? (input[i*2+j] - '0') : (input[i*2+j] - 'A' + 10));
        }
    }
    
    SumVersionOperator op;
    op.version = 0;
    op.type = 255;
    op.lengthType = 1;
    op.length = 1;
    uint32_t bitOffset = 0;
    operatorValue(&op, data, bitOffset);
    cout << op.getValue() << endl;

    SumOperator op2;
    op2.content = op.content;
    cout << op2.getValue();
}
