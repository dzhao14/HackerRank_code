#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	string steps;
	cin >> steps;
	int l = 0; int c = 0; bool v = false;
	for (int i=0 ; i<steps.size(); i++) {
		if (steps[i] == 'U') {
			l += 1;
		}
		else {
			l -= 1;
		}
		if (!v && l == -1) {
			v = true;
			c += 1;
		}
		if (v && l == 0) {
			v = false;
		}
	}
	cout << c;
}

