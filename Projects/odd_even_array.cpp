#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int size = 10;
    int even[size], odd[size];  // when it is not initialize, it will contain random numbers !!!
    int oddcount = 0, evencount = 0;

    for (int i = 0; i < size; i++) {
        if (arr[i]%2 == 0) {
            even[evencount] = arr[i];  // only those are even will enter array
            // guaruntee array size is that of the even numbers
            evencount++;
        } else {
            odd[oddcount] = arr[i];
            oddcount++;
        }
    }

    cout << "The even numbers in this array are: " << endl;
    for (int i = 0; i < evencount; i++) {
        cout << even[i] << " ";
    }

    cout << endl << "The odd numbers in this array are: " << endl;
    for (int i = 0; i < oddcount; i++) {
        cout << odd[i] << " ";
    }

    return 0;
}