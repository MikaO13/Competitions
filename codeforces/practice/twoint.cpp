#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long a, b;
        cin >> a >> b;
        int remainder = abs(a-b) % 10;
        if (remainder > 0) {
            cout << 1 + abs(a-b)/10 << endl;
        } else {
            cout << abs(a-b)/10 << endl;
        }
    }
    return 0;
}