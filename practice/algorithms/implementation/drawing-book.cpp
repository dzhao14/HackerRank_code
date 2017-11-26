#include <iostream>
using namespace std;

int main() {

	int n, p;
	cin >> n >> p;
	int b=0; int i=1; int f=0;
	while (i < p) {
		i += 2;
		f += 1;
	}
	if (n % 2 == 1) {
		i = n-1;
	}
	else {
		i = n;
	}
	while (i > p) {
		i -= 2;
		b += 1;
	}

	cout << min(f,b);
	return 0;
}
