#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main() {
    int qtdBlocos, alturaMaxima, bloco, pontuacao = 0, i;
    queue <int> filaTetris;
    stack <int> pilhaTetris;
    cin >> qtdBlocos >> alturaMaxima;
    for (i = 0; i < qtdBlocos; i++) {
        cin >> bloco;
        filaTetris.push(bloco);
    }
    i = 0;
    while (i < qtdBlocos) {
        if (pilhaTetris.empty()) {
            pilhaTetris.push(filaTetris.front());
            filaTetris.pop();
        }
        else if (pilhaTetris.size() == alturaMaxima) {
            break;
        }
        else if ((filaTetris.front() + pilhaTetris.top()) == 111) {
            pontuacao += 10;
            filaTetris.pop();
            pilhaTetris.pop();
        }
        else {
            pilhaTetris.push(filaTetris.front());
            filaTetris.pop();
        }
        i++;
    }
    if (pilhaTetris.size() == alturaMaxima) {
        cout << "game over" << endl;
    }
    else {
        cout << pontuacao;
    }
    return 0;
}