#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    int numOfensas, qtdMensagens, qtdPalavras, i, j;
    string palavra, mensagemOriginal, mensagemCensurada;
    set <string> ofensas, palavrasOfensivas, palavrasNaoOfensivas;
    vector <string> mensagens;
    cin >> numOfensas >> qtdMensagens;
    for (i = 0; i < numOfensas; i++) {
        cin >> palavra;
        ofensas.insert(palavra);
    }
    for (i = 0; i <= qtdMensagens; i++) {
        getline(cin, mensagemOriginal);
        mensagemOriginal += ' ';
        qtdPalavras = mensagemOriginal[0];
        int tamMensagem = mensagemOriginal.size();
        palavra.clear();
        for (j = 2; j < tamMensagem; j++) {
            if (mensagemOriginal[j] != ' ') {
                palavra += mensagemOriginal[j];
            }
            else {
                if (ofensas.count(palavra) == 1) {
                    mensagemCensurada.append("bobba ");
                    palavrasOfensivas.insert(palavra);
                }
                else {
                    palavrasNaoOfensivas.insert(palavra);
                    palavra += ' ';
                    mensagemCensurada.append(palavra);
                }
                palavra.clear();
            }
        }
        mensagemCensurada.resize(tamMensagem);
        mensagens.push_back(mensagemCensurada);
        mensagemCensurada.clear();
    }
    for (i = 0; i <= qtdMensagens; i++) {
        cout << mensagens[i] << endl;
    }
    cout << palavrasNaoOfensivas.size() << " " << palavrasOfensivas.size() << endl;
    return 0;
}