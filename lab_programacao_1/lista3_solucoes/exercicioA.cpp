#include <iostream>
#include <vector>

using namespace std;

bool pesquisaLinear(int elemento, vector <int> vetor) {
        int i, tam = vetor.size();
        for (i = 0; i < tam; i++) {
            if (vetor[i] == elemento) {
                return true;
                break;
            }
            else {
                continue;
            }
        }
        return false;
    }

int main() {
    int qtdCartas, i;
    cin >> qtdCartas;
    vector <int> baralho(qtdCartas);
    vector <int> cartasExodia(5);
    for (i = 0; i < qtdCartas; i++) {
        cin >> baralho[i];
    }
    for (i = 0; i < 5; i++) {
        cin >> cartasExodia[i];
    }    
    i = 0;
    bool encontrou;
    while (i < 5) {
        encontrou = pesquisaLinear(cartasExodia[i], baralho);
        if (encontrou == false) {
            cout << "Voce perdeu Yugi" << endl;
            break;
        }
        else {
            i++;
        }
    }
    if (encontrou) {
        cout << "Exodia Obliterar" << endl;
    }
    return 0;
}