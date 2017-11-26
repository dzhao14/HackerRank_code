#include <iostream>
using namespace std;

int main() {
	int n, v; int m = 0;
	cin >> n;
	int vals[n];
	int counts[n+1] = {0};
	for (int i=0; i<n; i++) {
		cin >> v;
		vals[i] = v;
		counts[v] += 1;
	}
	for (int i=1; i<n+1; i++) {
		m = max(m, counts[i] + counts[i-1]);
	}
	cout << m;
	return 0;
}
