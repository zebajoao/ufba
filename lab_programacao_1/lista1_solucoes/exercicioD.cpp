#include <iostream>

using namespace std;

int main() {
    int n, i;
    int cont = 0;
    char c;
    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> c;
        if (c == 'E') {
            cont++;
        }
    }
    if (cont >= 5) {
        cout << "Rei dos Jogos!" << endl;
    }
    else {
        cout << "Perdeu :(" << endl;
    }
    return 0;
}