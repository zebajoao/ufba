#include <iostream>
#include <set>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int qtdEventos, qtdSegmentos, inicio, termino, tamanho, i;
    pair <int,int> parAtual, proximoPar;
    char evento;
    set < pair<int,int> > estacionamento;
    set < pair<int,int> > :: iterator it1, it2;
    vector <int> numSegmentos;
    cin >> qtdEventos;
    for (i = 0; i < qtdEventos; i++) {
        cin >> evento >> inicio >> termino;
        switch (evento) {
            case 'E':
                estacionamento.insert(make_pair(inicio,termino));
                tamanho = estacionamento.size();
                qtdSegmentos = 1;
                if (tamanho <= 1) {
                    numSegmentos.push_back(qtdSegmentos);
                    break;
                }
                else {
                    for (it1 = estacionamento.begin(); it1 != estacionamento.end(); it1++) {
                        it2 = it1++;
                        if (it2 == estacionamento.end()) {
                            break;
                        }
                        else if ((it2->first) - (it1->second) > 1) {
                            qtdSegmentos++;
                        }
                        else {
                            continue;
                        }
                    }
                    numSegmentos.push_back(qtdSegmentos);
                }
                break;
            case 'S':
                estacionamento.erase(make_pair(inicio,termino));
                tamanho = estacionamento.size();
                qtdSegmentos = 1;
                if (tamanho <= 1) {
                    numSegmentos.push_back(qtdSegmentos);
                    break;
                }
                else {
                    for (it1 = estacionamento.begin(); it1 != estacionamento.end(); it1++) {
                        it2 = it1++;
                        if (it2 == estacionamento.end()) {
                            break;
                        }
                        else if ((it2->first) - (it1->second) > 1) {
                            qtdSegmentos++;
                        }
                        else {
                            continue;
                        }
                    }
                    numSegmentos.push_back(qtdSegmentos);
                }
                break;
        }
    }
    for (i = 0; i < qtdEventos; i++) {
        cout << numSegmentos[i] << endl;
    }
    return 0;
}