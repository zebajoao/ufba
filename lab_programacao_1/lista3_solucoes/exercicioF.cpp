#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

bool comparacaoNome(pair <string, int> a, pair <string, int> b) {
    return a.first < b.first;
}

bool comparacaoNivel(pair <string, int> a, pair <string, int> b){
    return a.second < b.second;
}

int main() {
    int qtdPokemons, nivel, i;
    char formaClassificacao, ordemClassificacao;
    string nome;
    cin >> qtdPokemons >> formaClassificacao >> ordemClassificacao;
    vector <pair<string,int>> pokedex;
    for (i = 0; i < qtdPokemons; i++) {
        cin >> nome >> nivel;
        pokedex.push_back(make_pair(nome, nivel));
    }
    switch (formaClassificacao) {
        case 'N':
            stable_sort(pokedex.begin(), pokedex.end(), comparacaoNome);
            break;
        case 'L':
            stable_sort(pokedex.begin(), pokedex.end(), comparacaoNivel);
            break;
        default:
            break;
    }
    i = 0;
    if (ordemClassificacao == 'D') {
        reverse(pokedex.begin(), pokedex.end());
    }
    while (i < qtdPokemons) {
        cout << pokedex[i].first << ' ' << pokedex[i].second << endl;
        i++;
    }
    return 0;
}