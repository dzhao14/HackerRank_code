#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

vector<long> pf(long n) {
	vector<long> ans;
	if (n == 1)	 { return ans; }
	int d = 2; int m = 2;
	int cut = (int)sqrt(n);
	while (n > 1) {
		if (d > cut) {
			ans.push_back(n);
			break;
		}
		if (n%d == 0) {
			ans.push_back(d);
			n /= d;
			cut = (int)sqrt(n);
		}
		else {
			if (d > 3) {
				if (m == 0 || m == 4) {
					d += 1; m += 1;
				}
				else if (m == 2) {
					d += 3; m += 3;
				}
				else if (m == 3 || m == 5) {
					d += 2; m += 2;
				}
				else {
					d += 4; m += 4;
				}
				if (m > 5) { m -= 6;}
			}
			else {
				d += 1; m += 1;
			}
		}
	}
	return ans;
}
	

int main() {
	int n;
	long v;
	cin >> n;
	vector<long> sticks;
	long tot = 0; long c = 1;
	for (int i=0; i<n; i++) {
		cin>>v;
		sticks.push_back(v);
	}
	for (int i=0; i<n; i++) {
		c = 1;
		tot += c;
		vector<long> pfs = pf(sticks[i]);
		for (int j = pfs.size()-1; j >= 0; j--) {
			c *= pfs[j];
			tot += c;
		}
	}
	cout << tot;
	return 0;
}	
