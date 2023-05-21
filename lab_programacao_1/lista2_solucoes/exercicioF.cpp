#include <iostream>
#include <string>

using namespace std;

int main() {
    int qtdNumeros, numeroBuscado, i;
    cin >> qtdNumeros >> numeroBuscado;
    int vetorFibonacci[qtdNumeros];
    vetorFibonacci[0] = 0, vetorFibonacci[1] = 1;
    for (i = 2; i < qtdNumeros; i++) {
        vetorFibonacci[i] = vetorFibonacci[i-1] + vetorFibonacci[i-2];
    }
    int limEsquerdo, meio, limDireito, posicao;
    limEsquerdo = 0, limDireito = qtdNumeros - 1;
    while (limEsquerdo <= limDireito) {
        meio = (limEsquerdo + limDireito) / 2;
        if (numeroBuscado < vetorFibonacci[meio]) {
            limDireito = meio - 1;
        }
        else if (numeroBuscado > vetorFibonacci[meio]) {
            limEsquerdo = meio + 1;
        }
        else {
            posicao = meio + 1;
            break;
        }
    }
    if (limEsquerdo > limDireito) {
        cout << numeroBuscado << " nao existe" << endl;
    }
    else {
        cout << numeroBuscado << " esta na posicao " << posicao << endl;
    }
    return 0;
}