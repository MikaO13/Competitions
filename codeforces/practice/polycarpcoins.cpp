#include <iostream>
#include <string>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        if (n%3 == 0) {
            cout << std::to_string(n/3) + ' ' + std::to_string(n/3) << endl;
        } else if (n%3 == 1) {
            cout << std::to_string(n/3 + 1) + ' ' + std::to_string(n/3) << endl;
        } else {
            cout << std::to_string(n/3) + ' ' + std::to_string(n/3 + 1) << endl;
        }
    }
    return 0;
}