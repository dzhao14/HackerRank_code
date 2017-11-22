#include <iostream>
using namespace std;

int main() {

	int n, t;
	int m = -1;
	cin >> n;
	int num_per_type[5] = {0};
	for (int i=0; i<n; i++) {
		cin >> t;
		num_per_type[t-1] += 1;
	}
	for (int i = 0; i < 5; i++) {
		m = max(m, num_per_type[i]);
	}
	for (int i = 0; i < 5; i++) {
		if (num_per_type[i] == m) {
			cout << i+1;
			break;
		}
	}

	return 0;
}
