#include<stdio.h>
void printarr(int*A,int n){
for (int  i = 0; i < n; i++)
{
    printf("%d ",A[i]);
}printf("\n");

}void bubblesort(int*A,int n){
    int issorted;
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-1-i;j++){
            issorted=1;
         if(A[j]>A[j+1]){
             int temp;
             issorted=0;
             temp=A[j];
             A[j]=A[j+1];
             A[j+1]=temp;
         }   
        }
    }
    
}

int main(int argc, char const *argv[]){
    int A[]={7,4,9,3,5,2};
    int n=6;
    printarr(A,n);
    bubblesort(A,n);
    printarr(A,n);
    return 0;
}
