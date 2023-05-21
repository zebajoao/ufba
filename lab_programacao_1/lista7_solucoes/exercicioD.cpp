#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct planeta {
    string nome;
    int impostoCobrado;
};

int main() {
    int qtdPlanetas, custoImposto, totalPago = 0, posicao, i;
    string nomePlaneta;

    cin >> qtdPlanetas;
    vector <planeta> federacao(qtdPlanetas);
    vector <string> planetas;
    vector <string> :: iterator it;
    
    for (i = 0; i < qtdPlanetas; i++) {
        cin >> federacao[i].nome >> federacao[i].impostoCobrado;
        planetas.push_back(federacao[i].nome);
    }
    cin >> qtdPlanetas;
    for (i = 0; i < qtdPlanetas; i++) {
        cin >> nomePlaneta;
        if (binary_search(planetas.begin(), planetas.end(), nomePlaneta)) {
            it = lower_bound(planetas.begin(), planetas.end(), nomePlaneta);
            posicao = it - planetas.begin();
            totalPago += federacao[posicao].impostoCobrado;
        }
    }
    cout << totalPago;

    return 0;
}