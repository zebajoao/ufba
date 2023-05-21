#include <iostream>

using namespace std;

int main() {
    char zagueiro, goleiro, drible, chute;
    cin >> zagueiro >> goleiro;
    cin >> drible >> chute;
    if (zagueiro != drible) {
        cout << "Bloqueado" << endl;
    }
    else if (goleiro != chute) {
        cout << "Driblado \n" << "...e o goleiro pega" << endl;
    }
    else {
        cout << "Driblado \n" << "Gol" << endl;
    }
    return 0;
}