#include <iostream>
using namespace std;

int HCF(int a, int b, int count);

int main() {
    int num1, num2, count;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    if (num1 > num2) {
        count = num1;
    } else {
        count = num2;
    }

    printf("The HCF of %d and %d is %d" , num1, num2, HCF(num1, num2, count)) ;
    return 0;
}

int HCF(int a, int b, int c) {
    if (a%c == 0 && b%c == 0) {
        return c;
    } else {
        //c -= 1; // don't use count-- or count++ for these problem
        // they will evaluate first before adding or subtracting
        return HCF(a,b,c-1);
    }
}