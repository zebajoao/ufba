#include <iostream>
#include <map>
#include <utility>

using namespace std;

int main() {
    int qtdItens, preco, valorTotal, i;
    string produto;

    map <string,int> catalogo;
    map <string,int> :: iterator it;

    cin >> qtdItens;
    for (i = 0; i < qtdItens; i++) {
        cin >> produto >> preco;
        catalogo.insert(make_pair(produto,preco)); 
    }
    cin >> qtdItens;
    valorTotal = 0;
    for (i = 0; i < qtdItens; i++) {
        cin >> produto;
        it = catalogo.find(produto);
        if (it != catalogo.end()) {
            valorTotal += it->second;
        }
    }
    cout << valorTotal << endl;

    return 0;
}