#include <iostream>
using namespace std;

int main() {
	int s, n, m, t;
	cin >> s >> n >> m;
	int ks[n];
	for (int i=0; i<n; i++) {
		cin >> t;
		ks[i] = t;
	}
	int ms[m];
	for (int i=0; i<m; i++) {
		cin >> t;
		ms[i] = t;
	}
	int mx = -1;
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			if (ks[i] + ms[j] <= s) {
				mx = max(mx, ks[i]+ms[j]);
			}
		}
	}
	cout << mx;
	return 0;
}
