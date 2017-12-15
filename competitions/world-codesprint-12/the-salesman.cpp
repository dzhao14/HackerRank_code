#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int t, n, v;
	cin >> t;
	for (int i=0; i<t; i++) {
		cin >> n;
		vector<int> list;
		for (int j=0; j<n; j++) {
			cin >> v;
			list.push_back(v);
		}
		cout << *max_element(list.begin(), list.end()) - *min_element(list.begin(), list.end()) << "\n";
	}
	return 0;
}
