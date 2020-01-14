/*
 * 3 star
 * DP
 * 24420565	1330	City Game	Accepted	C++11	0.080	2020-01-14 09:07:05
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int m, n;
		cin >> m >> n;
		string cell;

		// create a map with wall at top and left
		vector<vector<char> > maps(m + 1 , vector<char> (n + 1, 'R'));
		for (int i = 1; i <= m; ++i) {
			for (int j = 1; j <= n; ++j) {
				cin >> cell;
				maps[i][j] = cell[0];
			}
		}

		vector<vector<int> > width(m + 1, vector<int> (n + 1, 0));
		for (int i = 1; i <= m; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (maps[i][j] == 'F') {
					width[i][j] = width[i][j - 1] + 1;
				}
			}
		}

		int maxArea = 0;
		for (int x = 1; x <= m; ++x) {
			for (int y = 1; y <= n; ++y) {
				int maxWidth = width[x][y];
				for (int z = x; maps[z][y] == 'F'; --z) {
					maxWidth = min(width[z][y], maxWidth);
					int Area = maxWidth * (x - z + 1);
					if (maxArea < Area) {
						maxArea = Area;
					}
				}
			}
		}
		cout << maxArea * 3 << endl;
	}
}
