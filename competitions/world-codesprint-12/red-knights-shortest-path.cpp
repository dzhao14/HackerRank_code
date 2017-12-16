//https://www.hackerrank.com/contests/world-codesprint-12/challenges/red-knights-shortest-path

#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
#include<assert.h>
using namespace std;

int main() {
	int n, i, j, u, v;
	cin >> n >> i >> j >> u >> v;
	int seen[n][n];
	for (int c=0; c < n; c++) {
		for (int d=0; d<n; d++) {
			seen[c][d] = 0;
		}
	}
	queue< pair<int, int> > visit;
	visit.push(make_pair(i, j));
	pair<int, int> parent[n][n];
	seen[i][j] = 1;
	while (visit.size() > 0) {
		pair<int, int> at = visit.front();
		int a = at.first;
		int b = at.second;
		visit.pop();
		if (at.first == u && at.second == v) {
			break;
		}
		if (a-2 >= 0 && b-1 >= 0 && seen[a-2][b-1] == 0) {
			parent[a-2][b-1] = at;
			visit.push(make_pair(a-2, b-1));
			seen[a-2][b-1] = 1;
		}
		if (a-2 >= 0 && b+1 < n && seen[a-2][b+1] == 0) {
			parent[a-2][b+1] = at;
			visit.push(make_pair(a-2, b+1));
			seen[a-2][b+1] = 1;
		}
		if (b+2 < n && seen[a][b+2] == 0) {
			parent[a][b+2] = at;
			visit.push(make_pair(a, b+2));
			seen[a][b+2] = 1;
		}
		if (a+2 < n && b+1 < n && seen[a+2][b+1] == 0) {
			parent[a+2][b+1] = at;
			visit.push(make_pair(a+2, b+1));
			seen[a+2][b+1] = 1;
		}
		if (a+2 < n && b-1 >= 0 && seen[a+2][b-1] == 0) {
			parent[a+2][b-1] = at;
			visit.push(make_pair(a+2, b-1));
			seen[a+2][b-1] = 1;
		}
		if (b-2 >= 0 && seen[a][b-2] == 0) {
			parent[a][b-2] = at;
			visit.push(make_pair(a, b-2));
			seen[a][b-2] = 1;
		}
	}
	if (seen[u][v] != 1) {
		cout << "Impossible";
	}
	else {
		vector< pair<int, int> > sol;
		sol.push_back(make_pair(u, v));
		int s = u; int f = v;
		while (parent[s][f].first != i && parent[s][f].second != j) {
			sol.push_back(parent[s][f]);
			int temp = parent[s][f].first;
			int temp2 = parent[s][f].second;
			s = temp;
			f = temp2;
		}
		int prevx = i; int prevy = j;
		cout << sol.size() << "\n";
		for (int k = sol.size()-1; k >= 0; k--) {
			int newx = sol[k].first; int newy = sol[k].second;
			if (newx+2 == prevx && newy+1 == prevy) {
				cout << "UL ";
			}
			else if (newx+2 == prevx && newy-1 == prevy) {
				cout << "UR ";
			}
			else if (newx == prevx && newy-2 == prevy) {
				cout << "R ";
			}
			else if (newx-2 == prevx && newy-1 == prevy) {
				cout << "LR ";
			}
			else if (newx-2 == prevx && newy+1 == prevy) {
				cout << "LL ";
			}
			else if (newx == prevx && newy+2 == prevy) {
				cout << "L ";
			}
			else {
				assert (1==2);
			}
			prevx = newx; prevy = newy;
		}
	}
	return 0;
}

