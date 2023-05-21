#include <iostream>
#include <vector>
#include <string>

using namespace std;

int  main () {
    int numFases, vidaTotal, vidaAtual, i, fase;
    bool sucesso = true;
    vector<int> jogo;
    cin >> numFases;
    for (i = 0; i < numFases; i++) {
        cin >> fase;
        jogo.push_back(fase);
    }
    cin >> vidaTotal;
    vidaAtual = vidaTotal;
    for (i = 0; i < numFases; i++) {
        if (jogo[i] == 0) {
            continue;
        }
        else if (jogo[i] > 1) {
            vidaAtual -= jogo[i];           
            if (vidaAtual < 1) {
                sucesso = false;
                break;
            }
            else {
                continue;
            }
        }
        else {
            vidaAtual = vidaTotal;
            continue;
        }
    }
    if (sucesso) {
        cout << "Yes, you can" << endl;
    }
    else {
        cout << "You Died" << endl;
    }
    return 0;
}