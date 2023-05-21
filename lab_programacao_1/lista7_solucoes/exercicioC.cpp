#include <iostream>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int qtdLivros, disponibilidade, i;
    string codigo;

    vector <pair<string,int>> arquivo;
    vector <string> codigos;
    vector <string> :: iterator it;

    cin >> qtdLivros;
    for (i = 0; i < qtdLivros; i++) {
        cin >> codigo >> disponibilidade;
        codigos.push_back(codigo);
        arquivo.push_back(make_pair(codigo,disponibilidade));
    }
    cin >> qtdLivros;
    for (i = 0; i < qtdLivros; i++) {
        cin >> codigo;
        if (arquivo.empty()) {
            cout << "Nao encontrado" << endl;
        }
        else if (binary_search(codigos.begin(), codigos.end(), codigo)) {
            it = lower_bound(codigos.begin(), codigos.end(), codigo);
            int posicao = it - codigos.begin();
            if (arquivo[posicao].second == 2) {
                cout << "Emprestado" << endl;
            }
            else {
                cout << "Disponivel" << endl;
            }
        }
        else {
            cout << "Nao encontrado" << endl;
        }
    }

    return 0;
}