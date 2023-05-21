#include <iostream>

using namespace std;

int main() {
    int qtdElementos, i, qtdPar = 0, qtdImpar = 0;
    cin >> qtdElementos;
    int sequencia[qtdElementos];
    for (i = 0; i < qtdElementos; i++) {
        cin >> sequencia[i];
    }
    for (i = 0; i < qtdElementos; i++) {
        if (sequencia[i] % 2 == 0) {
            qtdPar++;
        }
        else {
            qtdImpar++;
        }
    }
    int elementosPares[qtdPar], elementosImpares[qtdImpar];
    int j = 0, k = 0, l = 0;
    while (j < qtdElementos) {
        if (sequencia[j] % 2 == 0) {
            elementosPares[k] = sequencia[j];
            k++;
        }
        else {
            elementosImpares[l] = sequencia[j];
            l++;
        }
        j++;
    }
    for (i = 0; i < qtdPar; i++) {
        cout << elementosPares[i] << " ";
    }
    cout << "\n";
    for (i = 0; i < qtdImpar; i++) {
        cout << elementosImpares[i] << " ";
    }
    return 0;
}
