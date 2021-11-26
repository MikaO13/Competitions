#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    char s[1000];
    while (t--) {
        int n;
        cin >> n;
        cin >> s+1;
        int f=n+1;
        for (int i = 1; i <= n; ++i) {
            if (s[i] != '?') {
                f=i;
                break;
            }
        }
        for (int i=f-1; i>=1; --i) {
            if (s[i+1] == 'R') s[i] = 'B';
            else s[i] = 'R';
        }
        for (int i=f+1; i <= n; ++i) {
            if (s[i] == '?') {
                if (s[i-1]=='R') s[i] = 'B';
                else s[i] = 'R';
            }
        }
        printf("%s\n",s+1);
    }
}