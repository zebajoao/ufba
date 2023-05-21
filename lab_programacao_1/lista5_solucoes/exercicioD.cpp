#include <iostream>
#include <set>

using namespace std;

int main() {
    int qtdIngredientes, codigoIngrediente, i;
    bool sobrou = false, faltou = false;
    set <int> pocaoCorreta, pocaoFeita, ingredientesSobrou, ingredientesFaltou;
    set <int> :: iterator it;
    cin >> qtdIngredientes;
    for (i = 0; i < qtdIngredientes; i++) {
        cin >> codigoIngrediente;
        pocaoCorreta.insert(codigoIngrediente);
    }
    cin >> qtdIngredientes;
    for (i = 0; i < qtdIngredientes; i++) {
        cin >> codigoIngrediente;
        pocaoFeita.insert(codigoIngrediente);
    }
    it = pocaoFeita.begin();
    while (it != pocaoFeita.end()) {
        if (pocaoCorreta.count(*it) == 0) {
            ingredientesSobrou.insert(*it);
            sobrou = true;
        }
        it++;
    }
    it = pocaoCorreta.begin();
    while (it != pocaoCorreta.end()) {
        if (pocaoFeita.count(*it) == 0) {
            ingredientesFaltou.insert(*it);
            faltou = true;
        }
        it++;
    }
    if (!sobrou && !faltou) {
        cout << "Acertou tudo" << endl;
    }
    else {
        if (sobrou) {
            cout << "Sobrou:" << endl;
            for (it = ingredientesSobrou.begin(); it != ingredientesSobrou.end(); it++) {
                cout << *it << " ";
            }
            cout << endl;
        }
        if (faltou) {
            cout << "Faltou:" << endl;
            for (it = ingredientesFaltou.begin(); it != ingredientesFaltou.end(); it++) {
                cout << *it << " ";
            }
            cout << endl;
        }
    }
    return 0;
}