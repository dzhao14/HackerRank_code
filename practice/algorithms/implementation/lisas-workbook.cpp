#include <iostream>
using namespace std;

int main() {
	int n, k, t;
	cin >> n >> k;
	int ps[n];
	for (int i=0; i<n; i++) {
		cin >> t;
		ps[i] = t;
	}
	int s = 0;
	int p = 1;
	int onpage = k;
	for (int i=0; i<n; i++) {
		for (int j=1; j<=ps[i]; j++) {
			if (onpage == 0) {
				p += 1;
				onpage = k;
			}
			if (p == j) {
				s += 1;
			}
			onpage -= 1;
		}
		if (onpage != k) {
			p += 1;
		}
		onpage = k;
	}
	cout << s;
	return 0;
}
