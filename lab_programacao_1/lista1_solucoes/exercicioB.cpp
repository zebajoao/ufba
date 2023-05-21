#include <iostream>

using namespace std;

int main() {
    int numero_do_processo;
    cin >> numero_do_processo;
    if (numero_do_processo % 42 == 0) {
    cout << "Sim" << endl;
    }
    else {
    cout << "Nao" << endl;
    }
}