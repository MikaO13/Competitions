"""
ID: Mika.di1
LANG: C++
TASK: namenum
PROG: namenum
"""

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool isValid(string str, string input) {
    if (input.size() != str.size()) {
        return false;
    }
    for (int i = 0; i < input.size(); ++i) {
        int char_place = str[i] - 'A';
        if (char_place > 16) { // if > Q decrease by 1 bc no Q 
            char_place --;
        }
        int dict_place = 2+char_place/3;
        char dig = '0' + dict_place;
        if (dig != input[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    ofstream out("namenum.out");
    ifstream in("namenum.in");
    ifstream dict("dict.txt");

    string input;
    fin >> input;

    string word;
    int count = 0;

    while (dict >> word) {
        if (isValid(word, input)) {
            fout << data << endl;
            count ++;
        }
    }

    if (!count) {
        fout << "NONE" << endl;
    }
    return 0;
}