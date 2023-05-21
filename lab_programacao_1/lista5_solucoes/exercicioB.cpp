#include <iostream>
#include <set>

using namespace std;

int main() {
    int valorNova, valorRepetida, tamBaralho, carta, i, lucro;
    set <int> cartasNovas;
    cin >> valorNova >> valorRepetida >> tamBaralho;
    for (i = 0; i < tamBaralho; i++) {
        cin >> carta;
        cartasNovas.insert(carta);
    }
    lucro = (valorNova * cartasNovas.size()) + (valorRepetida * (tamBaralho - cartasNovas.size()));
    cout << lucro << endl;
    return 0;
}