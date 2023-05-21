#include <iostream>
#include <set>

using namespace std;

int main () {
    int qtdNumeros, numero, i;
    set <int> numerosDistintos;
    cin >> qtdNumeros;
    for (i = 0; i < qtdNumeros; i++) {
        cin >> numero;
        numerosDistintos.insert(numero);
    }
    cout << numerosDistintos.size() << endl;
    return 0;
}