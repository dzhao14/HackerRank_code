#include<iostream>
using namespace std;

int MOD = 1000000007;

int main() {
	int n, x, k;
	long p;
	cin >> n >> k >> x;
	if (x == 1) {
		p = k-1;
	}
	else {
		p = k-2;
	}
	long total = k-1;
	for (int i=2; i<n-1; i++) {
		total = (total * (k-1)) % MOD;
		p = (total - p) % MOD;
	}
	cout << p;
	return 0;
}
