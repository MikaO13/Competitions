#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    long long t;
    string s;
    map<char, long long> letcount;
    cin >> t;
    while (t--) {
        long long count=0, leftover=0;
        letcount.clear();
        cin >> s;
        for (long long i = 0; i < s.size(); i++) {
            letcount[s[i]] ++;
        }
        for (auto i:letcount) {
            if (i.second > 1) {
                count += 1; // red + green
            } else if (i.second == 1) {
                leftover += 1; // only one color got to match w/ another
            }
            //cout << i.first << " " << i.second << endl;
        }
        cout << count + (leftover/2) << endl;

    }
    return 0;
}