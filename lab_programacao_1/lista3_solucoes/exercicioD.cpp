#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int qtdCasais, idade, i;
    cin >> qtdCasais;
    vector<int> idadeHomens(qtdCasais);
    for (i = 0; i < qtdCasais; i++) {
        cin >> idade;
        idadeHomens[i] = idade;
    }
    stable_sort(idadeHomens.begin(), idadeHomens.end());
    reverse(idadeHomens.begin(), idadeHomens.end());
    vector<int> idadeMulheres(qtdCasais);
    for (i = 0; i < qtdCasais; i++) {
        cin >> idade;
        idadeMulheres[i] = idade;
    }
    stable_sort(idadeMulheres.begin(), idadeMulheres.end());
    i = 0;
    while (i < qtdCasais) {
        cout << idadeHomens[i] << ' ' << idadeMulheres[i] << endl;
        i++;
    }
    return 0;
}