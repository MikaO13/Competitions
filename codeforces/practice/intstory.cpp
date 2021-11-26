#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, count, maxcount=0;
        cin >> n;
        vector<string> words;
        for (int i=0; i < n; i++) {
            cin >> words[i];
        }
        for (char ch = 'a'; ch < 'f'; ch++) {
            vector<int> v;
            for (int i=0; i < n; i++) {
                int unique = 0;
                int other = 0;
                for (int j = 0; j < words[i].size(); j++) {
                    if (ch==words[i][j]) {
                        unique++;
                    } else {
                        other--;
                    }
                }
                if (unique > other) {
                    // hm this but make it so it tests all opportunities of word sets
                }
            }
        }
    }
}

// using a recursive helper 
// see if the words in using can be done, then add a word from remaining
// 