#include <iostream>

using namespace std;

int main() {
    int qtdLinhas, qtdColunas, i, j;
    bool virusPresente = false, virusAniquilado = false;
    cin >> qtdLinhas >> qtdColunas;
    int matrizAmostra[qtdLinhas][qtdColunas];
    for (i = 0; i < qtdLinhas; i++) {
        for (j = 0; j < qtdColunas; j++) {
            cin >> matrizAmostra[i][j];
        }
    }
    for (i = 1; i < qtdLinhas - 1; i++) {
        for (j = 1; j < qtdColunas - 1; j++) {
            if (matrizAmostra[i][j] == 0) {
                virusPresente = true;
                if (matrizAmostra[i-1][j] == matrizAmostra[i][j-1] == matrizAmostra[i][j+1] == matrizAmostra[i+1][j] == 1) {
                    virusAniquilado = true;
                break;
                }
            }
        }
        if (virusPresente) {
            break;
        }
    }
    if (virusPresente && virusAniquilado) {
        cout << i << " " << j;
    }
    else {
        cout << 0 << " " << 0;
    }
    return 0;
}