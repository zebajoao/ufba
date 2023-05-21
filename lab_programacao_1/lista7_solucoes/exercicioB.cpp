#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int qtdPlanetas, codigoPlaneta, i;

    vector <int> planetasVisitados;
    vector <int> :: iterator it;

    cin >> qtdPlanetas;
    for (i = 0; i < qtdPlanetas; i++) {
        cin >> codigoPlaneta;
        planetasVisitados.push_back(codigoPlaneta);
    }
    stable_sort(planetasVisitados.begin(), planetasVisitados.end());
    while (true) {
        cin >> codigoPlaneta;
        if (codigoPlaneta == 0) {
            break;
        }
        else if (binary_search(planetasVisitados.begin(), planetasVisitados.end(), codigoPlaneta)) {
            it = lower_bound(planetasVisitados.begin(), planetasVisitados.end(), codigoPlaneta);
            cout << it - planetasVisitados.begin() << endl;
        }
        else {
            cout << "Nao foi visitado ainda." << endl;
        }
    }

    return 0;
}