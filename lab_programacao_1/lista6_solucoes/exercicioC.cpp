#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

map <string,string> :: iterator findValue(map <string,string> mapa, string valor) {
    map <string,string> :: iterator it;
    for (it = mapa.begin(); it != mapa.end(); it++) {
        if (it->second == valor) {
            break;
        }
    }
    return it;
}

int main() {
    int qtdPalavras, qtdMensagens, i, j;
    char fonte, destino;
    string palavra, traducao;

    map <string,string> dicionario;
    map <string,string> :: iterator it_map;
    vector <string> mensagem;
    vector <string> :: iterator it_vector0;
    vector <vector<string>> fraseTraduzida;
    vector <vector<string>> :: iterator it_vector1;

    cin >> qtdPalavras >> qtdMensagens;
    for (i = 0; i < qtdPalavras; i++) {
        cin >> palavra >> traducao;
        dicionario.insert(make_pair(palavra,traducao));
    }
    if (dicionario.empty()) {
        return 0;
    }
    for (i = 0; i < qtdMensagens; i++) {
        cin >> fonte >> destino >> qtdPalavras;
        if (fonte == 'A' && destino == 'B') {
            j = 0;
            while (j < qtdPalavras) {
                cin >> palavra;
                it_map = dicionario.find(palavra);
                if (it_map != dicionario.end()) {
                    mensagem.push_back(it_map->second);
                }
                else {
                    mensagem.push_back(palavra);
                }
                j++;
            }
        }
        else if (fonte == 'B' && destino == 'A') {
            j = 0;
            while (j < qtdPalavras) {
                cin >> palavra;
                it_map = findValue(dicionario, palavra);
                if (it_map != dicionario.end()) {
                    mensagem.push_back(it_map->first);
                }
                else {
                    mensagem.push_back(palavra);
                }
                j++;
            }
        }
        else {
            j = 0;
            while (j < qtdPalavras) {
                cin >> palavra;
                mensagem.push_back(palavra);
                j++;
            }
        }        
        fraseTraduzida.push_back(mensagem);
        mensagem.clear();
    }
    for (it_vector1 = fraseTraduzida.begin(); it_vector1 != fraseTraduzida.end(); it_vector1++) {
        mensagem = *it_vector1;
        for (it_vector0 = mensagem.begin(); it_vector0 != mensagem.end(); it_vector0++) {
            cout << *it_vector0 << ' ';
        }
        cout << endl;
    }

    return 0;
}