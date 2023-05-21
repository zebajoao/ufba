#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int qtdPlanetasGalaxia, qtdPlanetasVisitados, posicao, distancia, total, i, j, x, y;
    string codigo;

    vector <vector<int>> distancias;
    vector <int> distanciaEntrePlanetas, posicoes;
    vector <string> galaxia;
    vector <string> :: iterator it;

    posicoes.push_back(0);
    cin >> qtdPlanetasGalaxia;
    for (i = 0; i < qtdPlanetasGalaxia; i++) {
        cin >> codigo;
        galaxia.push_back(codigo);
    }
    cin >> qtdPlanetasVisitados;
    for (i = 0; i < qtdPlanetasVisitados; i++) {
        cin >> codigo;
        it = lower_bound(galaxia.begin(), galaxia.end(), codigo);
        posicao = it - galaxia.begin();
        posicoes.push_back(posicao);
    }
    for (i = 0; i < qtdPlanetasGalaxia; i++) {
        for (j = 0; j < qtdPlanetasGalaxia; j++) {
            cin >> distancia;
            distanciaEntrePlanetas.push_back(distancia);
        }
        distancias.push_back(distanciaEntrePlanetas);
        distanciaEntrePlanetas.clear();
    }
    total = 0;
    for (i = 0; i < posicoes.size() - 1; i++) {
        x = posicoes[i];
        y = posicoes[i+1];
        total += distancias[x][y];
    }
    cout << total << endl;

    return 0;
}