#include <iostream>
using namespace std;

int LCM(int a, int b, int count);

int main() {
    int num1, num2, count;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    if (num1 > num2) {
        count = num1;
    } else {
        count = num2;
    }

    printf("The LCM of %d and %d is %d", num1, num2, LCM(num1,num2,count));
    return 0;
}

int LCM(int a, int b, int c) {
    if (c%a == 0 && c%b == 0) {
        return c;
    } else {
        return LCM(a,b,c+1);
    }
}