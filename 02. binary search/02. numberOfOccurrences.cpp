#include <bits/stdc++.h>

using namespace std;

// #define int long long int

void solve() {
	vector<int> v = {1, 1, 2, 2, 2, 2, 3, 3};

	int size = v.size();


	cout << upper_bound(v.begin(), v.end(), 2) - lower_bound(v.begin(), v.end(), 2) << endl;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#ifndef ONLINE_JUDGE
	freopen("input.txt",  "r",  stdin);
	freopen("output.txt", "w", stdout);
#endif

	clock_t z = clock();

	int t = 1;
	// cin >> t;
	while (t--) solve();

	cerr << "Run Time : " << ((double)(clock() - z) / CLOCKS_PER_SEC);

	return 0;
}