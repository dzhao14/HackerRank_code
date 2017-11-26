#include <iostream>
using namespace std;

int main() {
	int q, x, y, z, dx, dy;
	cin >> q;
	for (int i=0; i<q; i++) {
		cin >> x >> y >> z;
		dx = abs(z-x);
		dy = abs(z-y);
		if (dx < dy) {
			cout << "Cat A" << "\n";
		}
		if (dx > dy) {
			cout << "Cat B" << "\n";
		}
		if (dx == dy) {
			cout << "Mouse C" << "\n";
		}
	}
	return 0;
}
