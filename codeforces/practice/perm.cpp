#include <iostream>
#include <string>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        std::string out = std::to_string(n) + ' ';
        if (n != 2) {
            for (int i = 1; i < n-1; ++i) {
                out += std::to_string(i) + ' ';
            }
        }
        out += std::to_string(n-1);
        cout << out << endl;
    }
    return 0;
}