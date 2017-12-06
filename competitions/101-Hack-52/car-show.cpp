//https://www.hackerrank.com/contests/101hack52/challenges/car-show

#include<iostream>
#include<vector>
#include<cassert>
using namespace std;

int A = 1000001;

int main() {
	int n, q, v, l, r;
	long tr, t;
	cin >> n >> q;
	int *models = new int[n];
	int *fur = new int[n];
	int *seen = new int[A];
	for (int i=0; i<A; i++) { seen[i] =0;}
	int *prev = new int[A];
	for (int i=0; i<n; i++) {
		cin >> v;
		models[i] = v;
	}

	int s = 0; int f = 0;
	while (s < n) {
		assert (s<=f);
		cout << s << " " << f;
		if (f < n && seen[models[f]] == 0) {
			fur[s] += 1;
			prev[models[f]] = f;
			seen[models[f]] = 1;
			f += 1;
		}
		else if (f<n && seen[models[f]] == 1) {
			seen[models[f]] = 0;
			s += 1;
			assert(prev[models[f]] >= s)
			while (s != prev[models[f]]) {
				fur[s] = fur[s-1] - 1;
				seen[models[s]] = 0;
				s += 1;
			}
		}
		else if (f == n && s+1 != n) {
			fur[s+1] = fur[s] - 1;
			s += 1;
		}
		else {
			s += 1;
		}
	}

	for (int i=0; i<q; i++) {
		cin >> l >> r;
		t=0;
		for (int j=l; j<=r; j++) {
			tr = fur[j]*(fur[j]+1)/2;
			t += tr;
		}
		cout << t;
	}
	return 0;
}


