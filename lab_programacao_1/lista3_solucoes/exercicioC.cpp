#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int qtdAlunos, i;
    cin >> qtdAlunos;
    string aluno;
    vector <string> alunos(qtdAlunos);
    for (i = 0; i < qtdAlunos; i++) {
        cin >> aluno;
        alunos[i] = aluno;
    }
    stable_sort(alunos.begin(), alunos.end());
    i = 0;
    while (i < qtdAlunos) {
        cout << alunos[i] << endl;
        i++;
    }
    return 0;
}