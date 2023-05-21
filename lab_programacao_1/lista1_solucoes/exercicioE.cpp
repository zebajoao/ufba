#include <iostream>

using namespace std;

int main() {
    int limiteDePressao, pressaoInterna;
    int alarme = 0;
    cin >> limiteDePressao;
    while (pressaoInterna != 0) {
        cin >> pressaoInterna;
        if (pressaoInterna > limiteDePressao) {
            alarme++;
            if (alarme == 1) {
                cout << "ALARME" << endl;
            }
        }
    }
    if (alarme == 0) {
        cout << "O Havai pode dormir tranquilo" << endl;
    }
    return 0;
}