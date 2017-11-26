#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, v, dx, y;
	cin >> n;
	int list[n];
	for (int i=0; i<n; i++) {
		cin >> v;
		list[i] = v;
	}
	for (int i=1; i <= n; i++) {
		dx = distance(list, find(list, list+n, i)) + 1;
		y = distance(list, find(list, list+n, dx)) + 1;
		cout << y << "\n";
	}
	return 0;
}
