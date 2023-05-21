#include <iostream>
#include <queue>

using namespace std;

int main() {
    int numProcessos, tempoVerificacao, tempoExecucao, tamFila, i, Q = 1;
    queue <int> filaProcessos;
    cin >> numProcessos >> tempoVerificacao;
    for (i = 0; i < numProcessos; i++) {
        cin >> tempoExecucao;
        filaProcessos.push(tempoExecucao);
    }
    i = 0;
    while (i < tempoVerificacao) {
        if (filaProcessos.empty()) {
            break;
        }
        filaProcessos.front()--;
        if (filaProcessos.front() <= 0) {
            filaProcessos.pop();
        }
        else {
            filaProcessos.push(filaProcessos.front());
            filaProcessos.pop();
        }
        i++;
    }
    if (filaProcessos.empty()) {
        cout << "pronto";
    }
    else {
        tamFila = filaProcessos.size();
        cout << tamFila << endl;
        for (i = 0; i < tamFila; i++) {
            cout << filaProcessos.front() << ' ';
            filaProcessos.pop();
        }
    }
    return 0;
}