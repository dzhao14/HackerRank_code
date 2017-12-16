#include<iostream>
#include<vector>
using namespace std;

int MOD = 1000000000;
int PRE[40] = {0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 227020800, 178291200, 674368000, 789888000, 428096000, 705728000, 408832000, 176640000, 709440000, 607680000, 976640000, 439360000, 984000000, 584000000, 768000000, 504000000, 616000000, 480000000, 880000000, 160000000, 280000000, 520000000, 200000000, 200000000, 400000000, 200000000, 800000000};

int main() {
	int n, m, v, type, l, r;
	cin >> n >> m;
	vector<int> A;
	vector<int> UP;
	vector<long> SUM;
	for (int i=0; i<n; i++) {
		cin >> v;
		A.push_back(v);
		UP.push_back(0);
		SUM.push_back(0);
	}
	vector< pair<int, pair<int, int> > > OP;
	for (int i=0; i<m; i++) {
		cin >> type >> l >> r;
		OP.push_back(make_pair(type, make_pair(l, r)));
	}
	int i = 0;
	bool recompute = true;
	while (i < OP.size()) {
		pair< int, pair< int, int> > op = OP[i];
		if (op.first == 1) {
			UP[op.second.first-1]++;
			if (op.second.second < UP.size()) { UP[op.second.second]--; }
			recompute = true;
		}
		else if (op.first == 2) {
			long sum = 0;
			if (recompute) {
				int up = 0;
				for (int j=0; j<n; j++) {
					up += UP[j];
					if (j > 0) {
						if (A[j] + up < 40) {
							SUM[j] = PRE[A[j]+up] + SUM[j-1];
						}
						else {
							SUM[j] = SUM[j-1];
						}
					}
					else {
						if (A[j] + up < 40) {
							SUM[j] = PRE[A[j] + up];
						}
						else {
							SUM[j] = 0;
						}
					}
				}
				recompute = false;
			}
			if (op.second.first != 1) {
				sum = (SUM[op.second.second-1] - SUM[op.second.first-1]) % MOD;
			}
			else {
				sum = SUM[op.second.second-1] % MOD;
			}
			cout << sum << "\n";
		}
		else {
			int up = 0;
			for (int j=0; j<op.second.first; j++) {
				up += UP[j];
			}
			A[op.second.first-1] = op.second.second - up;
			recompute = true;
		}
		i++;
	}

	return 0;
}
