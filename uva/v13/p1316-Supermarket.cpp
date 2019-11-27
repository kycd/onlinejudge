/*
 * 2.5 star
 * heap, greedy
 * 24251125	1316	Supermarket	Accepted	C++11	0.030	2019-11-27 07:17:28
 */
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Item {
	public:
		int profit, due;
		Item(int p = -1, int d = -1) : profit(p), due(d) {}
};

auto compare_item_due = [](Item x, Item y) {
	return x.due != y.due ? x.due < y.due : x.profit < y.profit;
};
auto compare_item_profit = [](Item x, Item y) {
	return x.profit != y.profit ? x.profit < y.profit : x.due < y.due;
};

int main() {
	int n;
	while (cin >> n) {
		priority_queue<Item, vector<Item>, decltype(compare_item_due)> warehouse(compare_item_due);
		int maxDue = -1;
		for (int i = 0; i < n; ++i) {
			int p, d;
			cin >> p >> d;
			if (d > maxDue) {
				maxDue = d;
			}
			Item* item = new Item(p, d);
			warehouse.push(*item);
		}

		priority_queue<Item, vector<Item>, decltype(compare_item_profit)> rack(compare_item_profit);
		int maxProfit = 0;
		for (int due = maxDue; due > 0; --due) {
			while (!warehouse.empty() && warehouse.top().due >= due) {
				rack.push(warehouse.top());
				warehouse.pop();
			}

			if (!rack.empty()) {
				maxProfit += rack.top().profit;
				rack.pop();
			}
		}
		cout << maxProfit << endl;
	}
	return 0;
}
