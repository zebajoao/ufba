#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main() {
    int qtdComponentes, componente, i, tamPilha, soma = 0;
    queue <int> todosComponentes;
    stack <int> componentesUteis;
    cin >> qtdComponentes;
    for (i = 0; i < qtdComponentes; i++) {
        cin >> componente;
        todosComponentes.push(componente);
    }
    i = 0;
    while (i < qtdComponentes) {
        if (todosComponentes.empty()) {
            break;
        }
        else if (todosComponentes.front() == -1) {
            todosComponentes.pop();
            if (componentesUteis.empty()) {
                continue;
            }
            else {
                componentesUteis.pop();
            }
        }
        else {
            componentesUteis.push(todosComponentes.front());
            todosComponentes.pop();
        }
        i++;
    }
    i = 0;
    tamPilha = componentesUteis.size();
    while (i < tamPilha) {
        soma += componentesUteis.top();
        componentesUteis.pop();
        i++;
    }
    cout << soma << endl;
    return 0;
}