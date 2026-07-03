#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> d;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            d.push_back(100 / a);
        }

        sort(d.begin(), d.end());

        int reach = 0;
        bool ok = true;

        for (int x : d) {
            if (x > reach + 1) {
                ok = false;
                break;
            }
            reach += 100;
        }

        cout << (ok ? "Yes" : "No") << '\n';
    }

    return 0;
}
