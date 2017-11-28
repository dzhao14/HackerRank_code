#include <iostream>
#include <string>
using namespace std;

int main() {

	int g, n, c, nx, pv;
	bool empty;
	string yes;
	string b;
	cin >> g;
	int counts[26] = {0};
	for (int i=0; i<g; i++) {
		cin >> n;
		cin >> b;
		for (int j=0; j<26; j++) {
			counts[j] = 0;
		}
		empty = false;
		for (int j=0; j<n; j++) {
			if (b[j] == '_') {
				empty = true;
			}
			else {
				c = (int)b[j] - 'A';
				counts[c] += 1;
			}
		}
		if (!empty && n > 1) {
			yes = "YES";
			for (int j=0; j<n; j++) {
				c = (int)b[j] - 'A';
				if (j == 0) {
					nx = (int)b[j+1] - 'A';
					if (c != nx) {
						yes = "NO";
					}
				}
				else if (j == n-1) {
					pv = (int)b[j-1] - 'A';
					if (c != pv) {
						yes = "NO";
					}
				}
				else {
					nx = (int)b[j+1] - 'A';
					pv = (int)b[j-1] - 'A';
					if (c != nx && c != pv) {
						yes = "NO";
					}
				}
			}
			cout << yes << "\n";
		}
		else if (!empty && n == 1) {
			cout << "NO" << "\n";
		}
		else {
			yes = "YES";
			for (int j=0; j<26; j++) {
				if (counts[j] == 1) {
					yes = "NO";
					break;
				}
			}
			cout << yes << "\n";
		}
	}

	return 0;
}
