#include <bits/stdc++.h>

using namespace std;

int main() {
	int h, w;
	cin >> h >> w;
	int table[h][w];
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			int val;
			cin >> val;
			table[i][j] = val;
		}
	}

	int area = 2 * w * h;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (i == 0) {
				area += table[i][j];
			}
			if (j == 0) {
				area += table[i][j];
			}
			if (i == h - 1) {
				area += table[i][j];
			}
			if (j == w - 1) {
				area += table[i][j];
			}
			if (i != 0) {
				area += max(0, table[i][j] - table[i-1][j]);
			}
			if (j != 0) {
				area += max(0, table[i][j] - table[i][j-1]);
			}
			if (i != h-1) {
				area += max(0, table[i][j] - table[i+1][j]);
			}
			if (j != w-1) {
				area += max(0, table[i][j] - table[i][j+1]);
			}
		}
	}
	cout << area;

	return 0;
}
