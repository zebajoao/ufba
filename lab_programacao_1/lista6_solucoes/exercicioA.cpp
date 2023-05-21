#include <iostream>
#include <map>
#include <string>
#include <utility>

using namespace std;

int main() {
    int numLinhas, qtdOcorrencias, qtdPalavras, i, j;
    string frase, palavra;
    map <string,int> palavras;
    map <string,int> :: iterator it;
    pair <string,int> ocorrencia;
    cin >> numLinhas;
    for (i = 0; i <= numLinhas; i++) {
        getline(cin, frase);
        frase += ' ';
        int tamanho = frase.size();
        for (j = 0; j < tamanho; j++) {
            if (frase[j] != ' ') {
                palavra += frase[j];
            }
            else if (palavras.count(palavra)) {
                it = palavras.find(palavra);
                it->second++;
                palavra.clear();
            }
            else {
                qtdOcorrencias = 1;
                ocorrencia.first = palavra;
                ocorrencia.second = qtdOcorrencias;
                palavras.insert(ocorrencia);
                palavra.clear();
            }
        }
    }
    qtdPalavras = 0;
    for (it = palavras.begin(); it != palavras.end(); it++) {
        if (it->second == 1) {
            qtdPalavras++;
        }
        else {
            palavras.erase(it);
        }
    }
    cout << qtdPalavras;
    if (qtdPalavras > 0) {
        for (it = palavras.begin(); it != palavras.end(); it++) {
            cout << it->first << endl;
        }
    }
    return 0;
}