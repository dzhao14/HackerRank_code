#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
	int q, n;
	long v;
	bool print;
	cin >> q;
	for (int i=0; i<q; i++) {
		cin >> n;
		long long rs[n];
		long long cs[n];
		for (int j=0; j<n; j++) {
			cs[j] = 0;
			rs[j] = 0;
		}
		for (int j=0; j<n; j++) {
			for (int k=0; k<n; k++) {
				cin >> v;
				rs[j] += v;
				cs[k] += v;
			}
		}
		print = true;
		sort(rs, rs+n);
		sort(cs, cs+n);
		for (int j=0; j<n; j++) {
			if (rs[j] != cs[j]) {
				cout << "Impossible" << "\n";
				print = false;
				break;
			}
		}
		if (print) { cout << "Possible" << "\n";}
	}
	return 0;
}
