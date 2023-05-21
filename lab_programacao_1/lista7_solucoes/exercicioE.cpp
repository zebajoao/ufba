#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int largura, comprimento, altura, qtdConsultas, numHoras, partesInundadas, i, j;
    
    vector <vector<int>> partes;
    vector <int> alturaDasPartes;
    vector <int> :: iterator it_0;

    cin >> largura >> comprimento;
    for (i = 0; i < largura; i++) {
        for (j = 0; j < comprimento; j++) {
            cin >> altura;
            alturaDasPartes.push_back(altura);
        }
        stable_sort(alturaDasPartes.begin(), alturaDasPartes.end());
        partes.push_back(alturaDasPartes);
        alturaDasPartes.clear();
    }
    cin >> qtdConsultas;
    for (i = 0; i < qtdConsultas; i++) {
        cin >> numHoras;
        partesInundadas = 0;
        j = 0;
        while (j < largura) {
            it_0 = upper_bound(partes[j].begin(), partes[j].end(), numHoras);
            partesInundadas += (it_0 - partes[j].begin());
            j++;
        }
        cout << partesInundadas << endl;
    }

    return 0;
}