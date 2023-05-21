#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int main() {
    int qtdPessoasPorFila, contador = 0, i, tam;
    string nome;
    char genero;
    pair<string,char> *temporario;
    queue < pair<string,char> > filaMasculina;
    queue < pair<string,char> > filaFeminina;
    cin >> qtdPessoasPorFila;
    for (i = 0; i < qtdPessoasPorFila * 2; i++) {
        cin >> nome >> genero;
        if (i < qtdPessoasPorFila) {
            filaFeminina.push(make_pair(nome,genero));
        }
        else {
            filaMasculina.push(make_pair(nome,genero));
        }
    }
    i = 0;
    while (i < qtdPessoasPorFila) {
        if (filaFeminina.empty()) {
            break;
        }
        else if (filaFeminina.front().second == 'M') {
            temporario = &filaFeminina.front();
            filaFeminina.push(make_pair(temporario->first, temporario->second));
            filaFeminina.pop();
        }
        else {
            temporario = &filaFeminina.front();
            filaMasculina.push(make_pair(temporario->first, temporario->second));
            filaFeminina.pop();
            contador++;
        }
        i++;
    }
    i = 0;
    while (i < qtdPessoasPorFila) {
        if (filaMasculina.empty()) {
            break;
        }
        else if (filaMasculina.front().second == 'H') {
            temporario = &filaMasculina.front();
            filaMasculina.push(make_pair(temporario->first, temporario->second));
            filaMasculina.pop();
        }
        else {
            temporario = &filaMasculina.front();
            filaFeminina.push(make_pair(temporario->first, temporario->second));
            filaMasculina.pop();
        }
        i++;
    }
    for (i = 0; i < contador; i++) {
        temporario = &filaMasculina.front();
        filaMasculina.push(make_pair(temporario->first, temporario->second));
        filaMasculina.pop();
    }
    cout << "Fila Feminina:" << endl;
    if (filaFeminina.empty()) {
        cout << "Vazia" << endl;
    }
    else {
        tam = filaFeminina.size();
        for (i = 0; i < tam; i++) {
            cout << filaFeminina.front().first << endl;
            filaFeminina.pop();
        }
    }
    cout << "Fila Masculina:" << endl;
    if (filaMasculina.empty()) {
        cout << "Vazia" << endl;
    }
    else {
        tam = filaMasculina.size();
        for (i = 0; i < tam; i++) {
            cout << filaMasculina.front().first << endl;
            filaMasculina.pop();
        }
    }
    return 0;
}
