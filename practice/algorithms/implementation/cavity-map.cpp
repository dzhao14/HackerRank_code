#include <iostream>
#include <string>
using namespace std;

int main() {

	int n;
	string row;
	cin >> n;
	string map[n];
	string f[n];
	for (int i=0; i<n; i++) {
		cin >> row;
		map[i] = row;
		f[i] = row;
	}
	int t, l, b, r, c;
	for (int i=1; i<n-1; i++) {
		for (int j=1; j<n-1; j++) {
			t = (int)map[i-1][j] - '0';
			l = (int)map[i][j-1] - '0';
			b = (int)map[i+1][j] - '0';
			r = (int)map[i][j+1] - '0';
			c = (int)map[i][j] - '0';
			if (c > t && c > l && c > b && c > r) {
				f[i][j] = 'X';
			}
		}
	}
	for (int i=0; i<n; i++) {
		cout << f[i] << "\n";
	}

	return 0;
}
