#include <iostream>
using namespace std;

int main() {
	int n, k, h; int c = 0;
	cin >> n >> k;
	for (int i=0; i<n; i++) {
		cin >> h;
		if (h > k) {
			c += h-k;
			k = h;
		}
	}
	cout << c;
	return 0;
}
