// AoC.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    string target = "PHVCVBFHCVPFKBNHKNBO";
    string rulesStr = "HK -> F|VN -> S|NB -> F|HF -> B|CK -> N|VP -> B|HO -> P|NH -> N|CC -> N|FC -> P|OK -> S|OO -> P|ON -> C|VF -> B|NN -> O|KS -> P|FK -> K|HB -> V|SH -> O|OB -> K|PB -> V|BO -> O|NV -> K|CV -> H|PH -> H|KO -> B|BC -> B|KC -> B|SO -> P|CF -> V|VS -> F|OV -> N|NS -> K|KV -> O|OP -> O|HH -> C|FB -> S|CO -> K|SB -> K|SN -> V|OF -> F|BN -> F|CP -> C|NC -> H|VH -> S|HV -> V|NF -> B|SS -> K|FO -> F|VO -> H|KK -> C|PF -> V|OS -> F|OC -> H|SK -> V|FF -> H|PK -> N|PC -> O|SP -> B|CB -> B|CH -> H|FN -> V|SV -> O|SC -> P|NP -> B|BB -> S|PV -> S|VB -> P|SF -> H|VC -> O|HN -> V|BF -> O|NO -> O|HP -> N|VV -> K|HS -> P|FH -> N|KB -> F|KF -> B|PN -> K|KH -> K|CN -> S|PP -> O|BP -> O|OH -> B|FS -> O|BK -> B|PO -> V|CS -> C|BV -> N|KP -> O|KN -> B|VK -> F|HC -> O|BH -> B|FP -> H|NK -> V|BS -> C|FV -> F|PS -> P";
    map<uint16_t, uint8_t> rules;

    for (int i = 0; i < rulesStr.length(); i += 8) {
        uint16_t key = (rulesStr[i]<<8) + rulesStr[i+1];
        rules.insert(pair<uint16_t, uint8_t>(key, rulesStr[i+6]));
    }

    /*
    // Slow Implementation
    char key[2] = {0,0};
    stringstream s1(target);
    stringstream s2;

    stringstream* start = &s1;
    stringstream* end = &s2;
    for (int i = 0; i < 40; i++) {
        end->str("");
        string str = start->str();
        for (int i = 0; i < str.length()-1; i++) {
            uint16_t key = (str[i]<<8) + str[i+1];
            *end << str[i];
            *end << rules[key];
        }
        *end << str[str.length()-1];

        swap(start, end);
    }

    string s = start->str();
    map<uint8_t, uint64_t> counts;
    for (int i = 0; i < s.length(); i++) {
        if (counts.count(s[i])) {
            counts[s[i]]++;
        }
        else {
            counts[s[i]] = 1;
        }
    }

    uint64_t smallest = 0;
    uint64_t highest = 0;
    for (auto const& kv : counts)
    {
        if (smallest == 0 || kv.second < smallest)
            smallest = kv.second;
        if (highest < kv.second)
            highest = kv.second;
    }
    cout << highest << " " << smallest << " " << highest-smallest << endl;
    */

    map<uint16_t, uint64_t> states;
    map<uint16_t, uint64_t> newStates;

    for (const auto& r : rules) {
        uint16_t s1 = r.first;
        uint16_t s2 = (r.first & (255 << 8)) + r.second;
        uint16_t s3 = (((uint16_t)r.second) << 8) + (r.first & 255);
        if (!states.count(s1))
            states[s1] = 0;
        if (!states.count(s2))
            states[s2] = 0;
        if (!states.count(s3))
            states[s3] = 0;
    }
    for(const auto& state : states)
        newStates[state.first] = 0;

    for (int i = 0; i < target.length()-1; i++) {
        uint16_t key = (target[i]<<8) + target[i+1];
        states[key]++;
    }

    auto* curState = &states;
    auto* nextState = &newStates;
    for (int i = 0; i < 40; i++) {
        for (const auto& r : rules) {
            uint16_t s1 = (r.first & (255 << 8)) + r.second;
            uint16_t s2 = (((uint16_t)r.second) << 8) + (r.first & 255);
            (*nextState)[s1] += (*curState)[r.first];
            (*nextState)[s2] += (*curState)[r.first];
            (*curState)[r.first] = 0;
        }
        swap(curState, nextState);
    }

    map<uint8_t, uint64_t> counts;
    for (auto const& kv : *curState) {
        uint8_t s1 = kv.first >> 8;
        uint8_t s2 = kv.first;
        if (counts.count(s1)) {
            counts[s1] += kv.second;
        }
        else {
            counts[s1] = kv.second;
        }
        if (counts.count(s2)) {
            counts[s2] += kv.second;
        }
        else {
            counts[s2] = kv.second;
        }
    }

    uint64_t smallest = 0;
    uint64_t highest = 0;
    for (auto const& kv : counts)
    {
        if (smallest == 0 || kv.second < smallest)
            smallest = kv.second;
        if (highest < kv.second)
            highest = kv.second;
    }
    cout << "Part Two: " << (highest+1)/2 - (smallest+1)/2 << endl;
}
