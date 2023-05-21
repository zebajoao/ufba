#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int main() {
    int qtdCartas, numRodadas, poderMonstro, i;
    queue <int> meusMonstros, monstrosOponente, cemiterio;
    cin >> qtdCartas;
    for (i = 0; i < qtdCartas; i++) {
        cin >> poderMonstro;
        meusMonstros.push(poderMonstro);
    }
    cin >> numRodadas;
    for (i = 0; i < numRodadas; i++) {
        cin >> poderMonstro;
        monstrosOponente.push(poderMonstro);
    }
    i = 0;
    while (i < numRodadas) {
        if (meusMonstros.empty() || monstrosOponente.empty()) {
            break;
        }
        else if (meusMonstros.front() >= monstrosOponente.front()) {
            meusMonstros.push(meusMonstros.front());
            meusMonstros.pop();
        }
        else {
            cemiterio.push(meusMonstros.front());
            meusMonstros.pop();
        }
        monstrosOponente.pop();
        i++;
    }
    cout << cemiterio.size();
    return 0;
}