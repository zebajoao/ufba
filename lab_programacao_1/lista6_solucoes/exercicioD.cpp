#include <iostream>
#include <map>
#include <string>
#include <utility>

using namespace std;

int main() {
    int qtdAlunos, qtdAulas, numMatricula, frequencia, i, j;

    map <int,int> listaDePresenca;
    map <int,int> :: iterator it;
    
    cin >> qtdAlunos >> qtdAulas;
    for (i = 0; i < qtdAlunos; i++) {
        cin >> numMatricula;
        frequencia = 0;
        listaDePresenca.insert(make_pair(numMatricula,frequencia));
    }
    for (i = 0; i < qtdAulas; i++) {
        cin >> qtdAlunos;
        j = 0;
        while (j < qtdAlunos) {
            cin >> numMatricula;
            it = listaDePresenca.find(numMatricula);
            (it->second)++;
            j++;
        }
    }
    for (it = listaDePresenca.begin(); it != listaDePresenca.end(); it++) {
        frequencia = it->second;
        double qtdFaltas = (1.00 * qtdAulas) - (1.00 * frequencia);
        if (qtdFaltas / qtdAulas > 0.25) {
            cout << it->first << ": RF" << endl;
        }
        else {
            cout << it->first << ": " << qtdFaltas << endl;
        }
    }

    return 0;
}