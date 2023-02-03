#include <iostream>
#include <cmath>
using namespace std;

int TotalGas(int gas, int spaceship, int people) {
    int actual_people;
    gas = gas - spaceship;
    actual_people = gas / people;
    return round(actual_people);
}

int main() {
    cout << "For 1000 gas, 500 spaceship and 200 for people, the program should return 2,and it actually returns: " << TotalGas(1000,500,200);
    return(TotalGas);
}