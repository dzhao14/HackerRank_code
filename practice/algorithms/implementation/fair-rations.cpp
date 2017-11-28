#include<iostream>
using namespace std;

int main() {

	int n, v;
	bool no = false;
	cin >> n;
	int b[n] = {0};
	for (int i=0; i<n; i++) {
		cin >> v;
		b[i] = v;
	}
	int c = 0;
	for (int i=0; i<n-1; i++) {
		if (b[i] % 2 == 1) {
			c += 2;
			b[i] += 1;
			b[i+1] += 1;
		}
	}
	if (b[n-1] % 2 == 1) {
		cout << "NO";
	}
	else {
		cout << c;
	}
	
	return 0;
}
