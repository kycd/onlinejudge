/*
 * 3 star
 * DP
 * 21813166    1317    Concert Hall Scheduling    Accepted    C++    0.200    2018-08-16 04:32:25
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

#define m 366

using namespace std;

class Application {
public:
    int fromDay, toDay, price;
    Application(int fromDay, int toDay, int price)
    {
        this->fromDay = fromDay;
        this->toDay = toDay;
        this->price = price;
    }

    char* toString()
    {
        char* msg = new char [50];
        sprintf(msg, "%d %d %d", this->fromDay, this->toDay, this->price);
        return msg;
    }
};

bool cmp(Application x, Application y)
{
    if (x.toDay == y.toDay) {
        return x.fromDay < y.fromDay;
    }
    return x.toDay < y.toDay;
}

class Blueprint {
public:
    int** contracts;
    int maxProfit;
    Blueprint()
    {
        contracts = new int* [m];
        for (int i = 0; i < m; ++i) {
            contracts[i] = new int [m];
            memset(contracts[i], -1, sizeof(int) * m);
        }

        maxProfit = 0;
    }

    void handle(Application x)
    {
        int ap1[m], ap2[m];
        memset(ap1, -1, sizeof(ap1));
        memset(ap2, -1, sizeof(ap2));

        for (int i = 0; i < x.fromDay; ++i) {
            for (int j = 0; j < x.fromDay; ++j) {
                if (contracts[i][j] > -1) {
                    ap1[i] = max(ap1[i], contracts[i][j] + x.price);
                    ap2[j] = max(ap2[j], contracts[i][j] + x.price);
                }
            }
            for (int j = x.fromDay; j < m; ++j) {
                if (contracts[i][j] > -1) {
                    ap2[j] = max(ap2[j], contracts[i][j] + x.price);
                }
            }
        }
        for (int i = x.fromDay; i < m; ++i) {
            for (int j = 0; j < x.fromDay; ++j) {
                if (contracts[i][j] > -1) {
                    ap1[i] = max(ap1[i], contracts[i][j] + x.price);
                }
            }
        }

        for (int k = 0; k < m; ++k) {
            contracts[k][x.toDay] = max(contracts[k][x.toDay], ap1[k]);
            contracts[x.toDay][k] = max(contracts[x.toDay][k], ap2[k]);
            maxProfit = max(maxProfit, ap1[k]);
            maxProfit = max(maxProfit, ap2[k]);
        }
    }
};

int main()
{
    int n;
    while (cin >> n && n) {
        vector<Application> vec;
        for (int i = 0; i < n; ++i) {
            int from, to, price;
            cin >> from >> to >> price;
            vec.push_back(Application(from, to, price));
        }

        sort(vec.begin(), vec.end(), cmp);
        Blueprint plan = Blueprint();

        plan.contracts[0][0] = 0;
        for (int i = 0; i < n; ++i) {
            plan.handle(vec[i]);
        }
        cout << plan.maxProfit << endl;
    }
    return 0;
}
