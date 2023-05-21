#include <iostream>
#include <string>

using namespace std;

int main() {
    string st, st1;
    int i, tam;
    bool palindromo = true;
    getline(cin, st);
    tam = st.size();
    for (i = 0; i < tam; i++) {
        st[i] = tolower(st[i]);
        if (st[i] != ' ') {
            st1 += st[i];
        }
    }
    tam = st1.size();
    int meio = tam / 2;
    for (i = 0; i < meio; i++) {
        if (st1[i] != st1[tam - 1 - i]) {
            palindromo = false;
            break;
        }
    }
    if (palindromo) {
        cout << "Palindromo" << endl;
    }
    else {
        cout << "!Palindromo" << endl;
    }
    return 0;
}