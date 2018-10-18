/*
 * 2 star
 * math
 * 22146951    1230    MODEX    Accepted    C++    0.000    2018-10-18 07:59:50
 */
#include <iostream>

using namespace std;

int modex(int x, int y, int n)
{
    if (y == 0) {
        return 1;
    }

    if (y % 2 == 1) {
        return ((modex(x * x % n, y / 2, n) % n) * (x % n)) % n;
    } else {
        return modex(x * x % n, y / 2, n) % n;
    }
    return 0;
}

int main()
{
    int t;
    cin >> t;

    while (t--) {
        int x, y, n;
        cin >> x >> y >> n;
        cout << modex(x % n, y, n) << endl;
    }
    return 0;
}
