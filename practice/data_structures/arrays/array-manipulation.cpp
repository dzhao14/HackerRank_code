#include <iostream>
using namespace std;

int main() {

	int n, m, a, b;
	cin >> n >> m;
	long k;
	long* counts = new long[n];
	for (int i=0; i<m; i++) {
		cin >> a >> b >> k;
		a -= 1; b -= 1;
		counts[a] += k;
		if (b < n-1) {
			counts[b+1] -= k;
		}
	}
	long ma = 0;
	long v = 0;
	for (int i=0; i < n; i++) {
		v += counts[i];
		ma = max(ma, v);
	}
	cout << ma;
	delete counts;

	return 0;
}
