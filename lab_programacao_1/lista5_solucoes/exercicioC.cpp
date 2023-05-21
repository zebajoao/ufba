#include <iostream>
#include <set>

using namespace std;

int main() {
    int qtdDias, nivelPokemon, nivelMinimoDia, i, k;
    set <int> pokemonsCapturados;
    set <int> :: iterator it;
    cin >> qtdDias;
    for (i = 0; i < qtdDias; i++) {
        for (k = 0; k < 6; k++) {
            cin >> nivelPokemon;
            pokemonsCapturados.insert(nivelPokemon);
        }
        cin >> nivelMinimoDia;
        for (it = pokemonsCapturados.begin(); it != pokemonsCapturados.end(); it++) {
            if (*it >= nivelMinimoDia) {
                continue;
            }
            else {    
                pokemonsCapturados.erase(it);
            }
        }
    }
    for (it = pokemonsCapturados.begin(); it != pokemonsCapturados.end(); it++) {
        cout << *it << " ";
    }
    return 0;
}