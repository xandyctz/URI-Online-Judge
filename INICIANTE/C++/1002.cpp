#include <iostream>
#include <iomanip> // para o setprecision (0.4f)

using namespace std;

int main(){
    double raio;
    cin >> raio;
    cout << fixed << setprecision(4);
    cout << "A=" << 3.14159*raio*raio << endl;
    return 0;
}
