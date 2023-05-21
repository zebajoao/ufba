#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    int qtdFeiticos, i;
    string feitico;
    
    vector <string> feiticosGerais, feiticosProibidos;

    cin >> qtdFeiticos;
    for (i = 0; i < qtdFeiticos; i++) {
        cin >> feitico;
        feiticosGerais.push_back(feitico);
    }
    cin >> qtdFeiticos;
    for (i = 0; i < qtdFeiticos; i++) {
        cin >> feitico;
        feiticosProibidos.push_back(feitico);
    }
    cin >> qtdFeiticos;
    for (i = 0; i < qtdFeiticos; i++) {
        cin >> feitico;
        if (binary_search(feiticosGerais.begin(), feiticosGerais.end(), feitico)) {
            cout << "Geral" << endl;
        }
        else {
            cout << "Proibido" << endl;
        }
    }
    
    return 0;
}