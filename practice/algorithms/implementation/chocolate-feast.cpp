#include <iostream>
using namespace std;

int main() {
	int t, n, c, m;
	cin >> t;
	for (int i=0; i < t; i++) {
		int cs = 0;
		int w = 0;
		cin >> n >> c >> m;
		cs += n / c;
		w += n / c;
		while (w >= m) {
			cs += w/m;
			w = (w/m) + (w % m);
		}
		cout << cs << "\n";
	}
	return 0;
}
