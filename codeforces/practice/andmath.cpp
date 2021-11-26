#include <iostream>
#include <string>

using namespace std;
int main() {
    int t, n, num, max;
    cin >> t;
    while (t--) {
        cin >> n;
        cin >> max;
        for (int i = 1; i < n; i++) {
            cin >> num;
            max = max&num;
        }
        cout << max << endl;
    }
}