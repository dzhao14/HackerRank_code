#include <bits/stdc++.h>
using namespace std;

bool validPrice(string price) {
	int sevens = 0;
	int fours = 0;

	for (int i = 0; i < price.length(); i++) {
		if (price[i] == '4') {
			fours += 1;
		}

		else if (price[i] == '7') {
			sevens += 1;
		}

		else {
			return false;
		}
	}
		return sevens == fours;
}

int main() {
	int n;
	int min_price = -1;
	string best_name = "-1";
	cin >> n;
	
	string name;
	string price;
	for(int i = 0; i < n; i++) {
		cin >> name;
		cin >> price;
		bool valid = validPrice(price);
		if (valid) {
			int p = atoi(price.c_str());
			if (min_price == -1) {
				min_price = p;
				best_name = name;
			}
			else {
				if (p < min_price) {
					min_price = p;
					best_name = name;
				}
			}
		}
	}
	cout << best_name;
	
	return 0;
}

