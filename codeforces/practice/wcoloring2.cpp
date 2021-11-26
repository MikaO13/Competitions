#include <iostream>
#include <string>
#include <map>
#include <array>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long n, k, count, curr=1; 
        map<long long, vector<long long>> numcount;
        numcount.clear();
        cin >> n >> k;
        long long out[2*(10^5)]; 
        for (int i = 0; i < n; ++i) {
            out[i] = 0;
        }
        long long num;
        for (long long i = 0; i < n; ++i) {
            cin >> num;
            numcount[num].push_back(i); 
        }
        for (auto i:numcount) {
            if (i.second.size() >= k) {
                count = 1;
                for (auto j = i.second.begin(); j != i.second.end(); ++j) {
                    out[j] = count;
                    count++;
                }
            } else {
                for (auto j = i.second.begin(); j != i.second.end(); ++j) {
                    out[j] = curr;
                    curr ++;
                    if (curr == k+1) {
                        curr = 1;
                    }
                }
            }
        }
        string toprint = "";
        for (int i = 0; i < n; ++i) {
            toprint += out[i] + " ";
        }

        cout << toprint.substr(0, toprint.size()-1) << endl;

        // loop through map - if > k then one of each and assign in corder
        // if not then assign to curr (should be looping through keys)
        // so no key will have the same color assigned twice
        // need to store index of somewhere and connected to the key
        // maybe another map? but need to loop through keys 
        // then increase curr and % k to have the colors loop
    }
    return 0;
}