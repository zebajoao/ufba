#include <iostream>

using namespace std;

int main() {
    int tabuleiro[8][8];
    int i, j, x, y;
    for (i = 0; i < 8; i++) {
        for (j = 0; j < 8; j++) {
            cin >> tabuleiro[i][j];
        }
    }
    cin >> x >> y;
    int qtdInimigos = 0;
    for (i = x - 1; i > -1; i--) {
        if (tabuleiro[i][y] != 1) {
            if (tabuleiro[i][y] == 0) {
                continue;
            }
            else {
                qtdInimigos++;
                break;
            }
        }
        else {
            break;
        }
    }
    for (i = x + 1; i < 8; i++) {
        if (tabuleiro[i][y] != 1) {
            if (tabuleiro[i][y] == 0) {
                continue;
            }
            else {
                qtdInimigos++;
                break;
            }
        }
        else {
            break;
        }
    }
    for (j = y - 1; j > -1; j--) {
        if (tabuleiro[x][j] != 1) {
            if (tabuleiro[x][j] == 0) {
                continue;
            }
            else {
                qtdInimigos++;
                break;
            }
        }
        else {
            break;
        }
    }
    for (j = y + 1; j < 8; j++) {
        if (tabuleiro[x][j] != 1) {
            if (tabuleiro[x][j] == 0) {
                continue;
            }
            else {
                qtdInimigos++;
                break;
            }
        }
        else {
            break;
        }
    }
    cout << qtdInimigos;
    return 0;
}