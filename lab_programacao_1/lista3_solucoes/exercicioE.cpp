#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

bool comparacao(pair <string, int> a, pair <string, int> b) {
    return a.second > b.second;
}

int main() {
    int arvoresCatalogadas, maxCortes, altura, i;
    string nomeEspecie;
    vector < pair<string,int> > catalogo;
    cin >> arvoresCatalogadas >> maxCortes;
    for (i = 0; i < arvoresCatalogadas; i++) {
        cin >> nomeEspecie >> altura;
        catalogo.push_back(make_pair(nomeEspecie, altura));
    }
    stable_sort(catalogo.begin(), catalogo.end(), comparacao);
    i = 0;
    while (i < maxCortes) {
        cout << catalogo[i].first << endl;
        i++;
    }
    return 0;
}