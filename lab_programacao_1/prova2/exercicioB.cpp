#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int qtdCorridas, qtdCavalos, cavalo, posicao, i, j;

    vector <int> listaDeCavalos;
    vector <int> :: iterator it;

    cin >> qtdCorridas;
    for (i = 0; i < qtdCorridas; i++) {
        cin >> qtdCavalos;
        for (j = 0; j < qtdCavalos; j++) {
            cin >> cavalo;
            listaDeCavalos.push_back(cavalo);
        }
        cin >> cavalo;
        it = upper_bound(listaDeCavalos.begin(), listaDeCavalos.end(), cavalo);
        posicao = it - listaDeCavalos.begin();
        cout << posicao - 1 << endl;
        listaDeCavalos.clear();
    }

    return 0;
}