#include <unordered_map>
#include <iostream>
#include <vector>
using namespace std;


long calcSums(int start, unordered_map<int, vector<int>> &graph, int* values, 
		int n, unordered_map<int, int>& parent, long* best) {

	int neib;
	long val = values[start];
	vector<int> neibs = graph.at(start);
	for (int i = 0; i < neibs.size(); i++) {
		neib = neibs[i];
		if (parent.at(start) != neibs[i]) {
			parent.insert({neib, start});
			val += calcSums(neib, graph, values, n, parent, best);
		}
	}
	best[start] = val;
	return val;
}
		

void solution(unordered_map<int, vector<int>>& graph, int* values, int n) {
	long best[n];
	unordered_map<int, int> parent;
	parent.insert({0,-1});
	calcSums(0, graph, values, n, parent, best);

	long m;
	m = abs(best[0] - best[1] - best[1]);
	for (int i = 2; i < n; i++) {
		m = min(m, abs(best[0] - best[i] - best[i]));
	}
	cout << m;
}


int main() {
	
	int n, val, u, v;
	cin >> n;
	int values[n];
	unordered_map<int, vector<int>> graph;
	for (int i = 0; i < n; i++) {
		cin >> val;
		values[i] = val;
		vector<int> empty;
		pair<int, vector<int>> p (i, empty);
		graph.insert(p);
	}
	for (int i = 0; i < n-1; i++) {
		cin >> u >> v;
		u -= 1; v -= 1;
		graph.at(u).push_back(v);
		graph.at(v).push_back(u);
	}

	solution(graph, values, n);
	
	return 0;
}
