// AoC.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

string getFile() {
    ifstream file("day15input.txt");
    return string((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
}

void splitIntoLines(string& input, vector<string>& lines) {
    int offset = 0;
    int id = 0;
    string substr;
    id = input.find('\n', offset);
    while (id != -1) {
        substr = input.substr(offset, id-offset);
        lines.push_back(substr);
        offset = id+1;
        id = input.find('\n', offset);
    }
    if (input.length()-offset > 0) {
        substr = input.substr(offset);
        lines.push_back(substr);
    }
}

void intMap(vector<string>& lines, vector<vector<int>>& map) {
    for (auto l : lines) {
        vector<int> lineInts;
        for (auto c : l) {
            lineInts.push_back(c - '0');
        }
        if(lineInts.size() > 0)
            map.push_back(lineInts);
    }
}

void intMap2(vector<string>& lines, vector<vector<int>>& map) {
    for(int y = 0; y < 5; y++)
        for (auto l : lines) {
            vector<int> lineInts;
            for (int x = 0; x < 5; x++)
                for (auto c : l) {
                    lineInts.push_back((c - '0' + x + y - 1)%9+1);
                }
            if (lineInts.size() > 0)
                map.push_back(lineInts);
        }
}

struct Pos {
    uint32_t x, y, score;

    bool operator<(const Pos& pos) const { return this->score < pos.score || this->score == pos.score && (this->x < pos.x || this->x == pos.x && this->y < pos.y); }
    bool operator>(const Pos& pos) const { return this->score > pos.score || this->score == pos.score && (this->x > pos.x || this->x == pos.x && this->y > pos.y); }
};

int scoreFromMap(vector<vector<int>>& map) {
    const int sizeX = map[0].size();
    const int sizeY = map.size();
    set<Pos> positions;
    positions.insert(Pos{ 0,0,0 });
    map[0][0] = 0;

    while (!positions.empty()) {
        auto nextPos = *positions.begin();
        positions.erase(positions.begin());

        if (nextPos.y == sizeY-1 && nextPos.x == sizeX-1) return nextPos.score;

        for (int i = -1; i <= 1; i++) {
            if (nextPos.x+i >= 0 && nextPos.x+i < sizeX && map[nextPos.y][nextPos.x+i] != 0) {
                positions.insert(Pos{ nextPos.x+i, nextPos.y, nextPos.score+map[nextPos.y][nextPos.x+i] });
                map[nextPos.y][nextPos.x+i] = 0;
            }
            if (nextPos.y+i >= 0 && nextPos.y+i < sizeY && map[nextPos.y+i][nextPos.x] != 0) {
                positions.insert(Pos{ nextPos.x, nextPos.y+i, nextPos.score+map[nextPos.y+i][nextPos.x] });
                map[nextPos.y+i][nextPos.x] = 0;
            }
        }
    }
    return 0;
}

int main()
{
    vector<string> lines;
    vector<vector<int>> map;
    string input = getFile();
    splitIntoLines(input, lines);
    intMap(lines, map);

    cout << "Part One: " << scoreFromMap(map) << endl;

    vector<vector<int>> map2;
    intMap2(lines, map2);
    cout << "Part Two: " << scoreFromMap(map2) << endl;
}
