#include <iostream>
using namespace std;

int main() {

	int n, d, m, s, v;
	cin >> n;
	int vals[n];
	for (int i=0; i<n; i++) {
		cin >> v;
		vals[i] = v;
	}
	cin >> d >> m;
	int ways = 0;
	for (int i=0; i<n-m+1; i++) {
		s = 0;
		for (int j=0; j<m; j++) {
			s += vals[j+i];
		}
		if (s == d) {
			ways += 1;
		}
	}
	cout << ways;

	return 0;
}
