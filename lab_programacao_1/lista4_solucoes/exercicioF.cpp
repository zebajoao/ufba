#include <iostream>
#include <queue>
#include <stack>
#include <utility>

using namespace std;

int main() {
    int linhas, qtdFeno, dataValidade, qtdNegociacoes, tam, i, j;
    char tipoNegociacao;
    stack < pair<int,int> > mercadoWinterfell, pilhaAuxiliar;
    cin >> linhas;
    for (i = 0; i < linhas; i++) {
        cin >> qtdFeno >> dataValidade;
        mercadoWinterfell.push(make_pair(qtdFeno,dataValidade));
    }
    cin >> qtdNegociacoes;
    for (i = 0; i < qtdNegociacoes; i++) {
        cin >> tipoNegociacao >> qtdFeno;
        switch (tipoNegociacao){
            case 'C':
                if (mercadoWinterfell.empty()) {
                    break;
                }
                else {
                    j = 0;
                    while (j < qtdFeno) {
                        if (mercadoWinterfell.empty()) {
                            break;
                        }
                        else if (mercadoWinterfell.top().first > 1) {
                            mercadoWinterfell.top().first--;
                        }
                        else {
                            mercadoWinterfell.pop();
                        }
                        j++;
                    }
                    break;
                }
            case 'V':
                cin >> dataValidade;
                while (true) {
                    if (mercadoWinterfell.empty()) {
                        mercadoWinterfell.push(make_pair(qtdFeno,dataValidade));
                        break;
                    }
                    else if (dataValidade > mercadoWinterfell.top().second) {
                        pilhaAuxiliar.push(mercadoWinterfell.top());
                        mercadoWinterfell.pop();
                        continue;
                    }
                    else if (dataValidade == mercadoWinterfell.top().second) {
                        mercadoWinterfell.top().first += qtdFeno;
                        break;
                    }
                    else {
                        mercadoWinterfell.push(make_pair(qtdFeno,dataValidade));
                        break;
                    }
                }
                j = 0;
                tam = pilhaAuxiliar.size();
                while (j < tam) {
                    mercadoWinterfell.push(pilhaAuxiliar.top());
                    pilhaAuxiliar.pop();
                    j++;
                }
                break;
            default:
                break;
        }
    }
    if (mercadoWinterfell.empty()) {
        cout << "Sem estoque" << endl;
    }
    else {
        tam = mercadoWinterfell.size();
        for (i = 0; i < tam; i++) {
            cout << mercadoWinterfell.top().first << ' ' << mercadoWinterfell.top().second << endl;
            mercadoWinterfell.pop();
        }
    }
    return 0;
}