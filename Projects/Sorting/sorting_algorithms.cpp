#include <stdio.h>
#include <stdlib.h>
#include <iostream>

// Print primitive datatypes
void print (auto input) {
  std::cout << input << std::endl;
}

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
  int i, j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  /* create temp arrays */
  int L[n1], R[n2];

  /* Copy data to temp arrays L[] and R[] */
  for (i = 0; i < n1; i++)
    L[i] = arr[l + i];
  for (j = 0; j < n2; j++)
    R[j] = arr[m + 1 + j];

  /* Merge the temp arrays back into arr[l..r]*/
  i = 0; // Initial index of first subarray
  j = 0; // Initial index of second subarray
  k = l; // Initial index of merged subarray
  while (i < n1 && j < n2)
  {
    if (L[i] <= R[j])
    {
      arr[k] = L[i];
      i++;
    }
    else
    {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  /* Copy the remaining elements of L[], if there are any */
  while (i < n1)
  {
    arr[k] = L[i];
    i++;
    k++;
  }

  /* Copy the remaining elements of R[], if there are any */
  while (j < n2)
  {
    arr[k] = R[j];
    j++;
    k++;
  }
}

/* l is for left index and r is right index of the sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
  if (l < r)
  {
    // Same as (l+r)/2, but avoids overflow for
    // large l and h
    int m = l + (r - l) / 2;

    // Sort first and second halves
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    merge(arr, l, m, r);
  }
}

/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
  int i, key, j;
  for (i = 1; i < n; i++)
  {
    key = arr[i];
    j = i - 1;

    /* Move elements of arr[0..i-1], that are
      greater than key, to one position ahead
      of their current position */
    while (j >= 0 && arr[j] > key)
    {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = key;
  }
}

void swap(int *xp, int *yp)
{
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

// A function to implement BubbleSort -- O(n^2)
void bubbleSort(int arr[], int n)
{
  // for (int i = 0; i < n; i++){
  //   printf("%d x", arr[i]);
  // }

    int i, j;
  for (i = 0; i < n - 1; i++)

    // Last i elements are already in place
    for (j = 0; j < n - i - 1; j++)
      if (arr[j] > arr[j + 1])
        swap(&arr[j], &arr[j + 1]);
}

// A function to implement SelectionSort -- O(n^2)
void selectionSort(int arr[], int n)
{
  int i, j, min_idx;

  // One by one move boundary of unsorted subarray
  for (i = 0; i < n - 1; i++)
  {
    // Find the minimum element in unsorted array
    min_idx = i;
    for (j = i + 1; j < n; j++)
      if (arr[j] < arr[min_idx])
        min_idx = j;

    // Swap the found minimum element with the first element
    swap(&arr[min_idx], &arr[i]);
  }
}

// A function to implement Quicksort -- O(n^2)
//partition function
int partition(int arr[], int low, int high)
{
  int pivot = arr[high]; // pivot
  int i = (low - 1);     // Index of smaller element

  for (int j = low; j <= high - 1; j++)
  {
    // If current element is smaller than or
    // equal to pivot
    if (arr[j] <= pivot)
    {
      i++; // increment index of smaller element
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i + 1], &arr[high]);
  return (i + 1);
}
void quickSort(int arr[], int low, int high)
{
  if (low < high)
  {
    /* pi is partitioning index, arr[p] is now at right place */
    int pi = partition(arr, low, high);

    // Separately sort elements before
    // partition and after partition
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}
