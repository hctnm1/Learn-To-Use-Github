#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
    /* code */
    int A[] = {9, 4, 4, 8, 7, 5, 6};
    int n = 7;
    print(A, n);

    mergesort(A, 0, 6);    
    printf("\n");
    print(A, n);
    return 0;
}
int print(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
}
int merge(int A[], int low, int high, int mid)
{
    int i, j, k;
    int B[100];
    i = low;
    j = mid + 1;
    k = low;
    while (i <= mid && j <= high)
    {
        if (A[i] < A[j])
        {
            B[k] = A[i];
            i++;
         k++;   
        }
        else
        {
            B[k] = A[j];
            j++;
           k++;
        } 
    }
    while (i <= mid)
    {
        B[k] = A[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        B[k] = A[j];
        k++;
        j++;
    }
    for (int i = low; i <= high; i++)
    {
        B[i]=A[i];
    }
    
}
int mergesort(int A[ ], int low, int high)
{
    if (low < high)
    {
        int mid = (low + high) / 2;
        mergesort(A, low, mid);
        mergesort(A, mid + 1, high);
        merge(A, mid, low, high);
    }
}
a