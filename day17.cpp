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

int minX = 153; // Use abs
int maxX = 199; // Use abs
int minY = -114;
int maxY = -75;

int calcMaxPos(int vel) {
	return vel*(vel+1) / 2;
}

int doesHitArea(int xVel, int yVel) {
	int x = 0;
	int y = 0;
	while (
		x <= maxX && // Can reach area
		y >= minY	 // Can reach area
		) {
		
		if (x >= minX && y <= maxY) {
			return true;
		}
		x += xVel;
		y += yVel;
		xVel = xVel > 0 ? xVel-1 : 0;
		yVel--;
	}
	return false;
}

int main()
{

	cout << calcMaxPos(-(minY+1)) << endl;

	// Find x to hit target area
	int minXVel = 0;
	bool inArea = false;
	while (!inArea) {
		minXVel++;
		int x = calcMaxPos(minXVel);
		inArea = x >= minX && x <= maxX;
	}

	int sum = 0;
	for (int yVel = minY; yVel < -minY; yVel++) {
		for (int xVel = maxX; xVel >= minXVel; xVel--) {
			sum += doesHitArea(xVel, yVel) ? 1: 0;
		}
	}
	cout << sum;
}
