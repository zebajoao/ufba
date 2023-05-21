#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int qtdPalavras, qtdTraducoes, i, j;
    string palavra, traducao, frase;
    vector <string> fraseTraduzida;
    vector <string> :: iterator it_vector;
    map <string,string> dicionario;
    map <string,string> :: iterator it_map;
    cin >> qtdPalavras;
    for (i = 0; i < qtdPalavras; i++) {
        cin >> palavra >> traducao;
        dicionario.insert(make_pair(palavra,traducao));
    }
    cin >> qtdTraducoes;
    for (i = 0; i < qtdTraducoes; i++) {
        cin >> palavra;
        it_map = dicionario.find(palavra);
        if (it_map != dicionario.end()) {
            fraseTraduzida.push_back(it_map->second);
        }
        else {
            fraseTraduzida.push_back(palavra);
        }
    }
    for (it_vector = fraseTraduzida.begin(); it_vector != fraseTraduzida.end(); it_vector++) {
        cout << *it_vector << ' ';
    }
    return 0;
}