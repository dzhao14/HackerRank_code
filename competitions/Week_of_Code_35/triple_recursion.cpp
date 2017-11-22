#include <bits/stdc++.h>

using namespace std;

void solution(int n, int m, int k) {
	int table[n][n];
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < n; j++) {
			if (i == j && i == 0) {
				table[0][0] = m;
			}
			else if (i == j) {
				table[i][j] = table[i-1][j-1] + k;
			}
			else if (i > j) {
				table[i][j] = a[i-1][j] - 1;
			}
			else {
				table[i][j] = a[i][j-1] - 1;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout >> table[i][j] >> " ";
		}
		cout >> "\n";
	}
}

int main() {
	int n, m, k;
	cin >> n >> m >> k;
	solution(n, m, k);
	return 0;
}
