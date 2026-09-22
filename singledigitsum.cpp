#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int total = n * k;

    while (to_string(total).length() > 1) {
        int totalSum = 0;
        while (total > 0) {
            totalSum += total % 10;
            total /= 10;
        }
        total = totalSum;
    }

    cout << total << endl;
    return 0;
}