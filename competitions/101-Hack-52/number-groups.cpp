#include<iostream>
using namespace std;

int main() {
	long k;
	cin >> k;
	long long start = k*(k-1)/2; 
	long long startv = start * 2 + 1;
	long long c = 0;
	for (long i=0; i<k; i++) {
		c += startv;
		startv += 2;
	}
	cout << c;
	return 0;
}
