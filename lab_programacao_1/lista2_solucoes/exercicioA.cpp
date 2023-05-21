#include <iostream>

using namespace std;

int main () {
    int qtdNumeros, primeirosValores, soma = 0;
    cin >> qtdNumeros;
    int valores[qtdNumeros];
    for (int i = 0; i < qtdNumeros; i++) {
        cin >> valores[i];
    }
    cin >> primeirosValores;
    for (int j = 0; j < primeirosValores; j++) {
        soma += valores[j];
    }
    if (soma % 2 == 0) {
        cout << "tutturu" << endl;
    }
    else {
        cout << "SERN" << endl;
    }
    return 0;
}