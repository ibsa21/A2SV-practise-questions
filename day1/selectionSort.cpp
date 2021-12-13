int select(int arr[], int i)
{
    // code here such that selecionSort() sorts arr[]
    int min = arr[i];
    int minIndex = i;
    for(int j = i; j < sizeof(arr)/ sizeof(arr[i]); i++) {
        if(min > arr[j]) {
            min = arr[j];
            minIndex = j;
        }
    }
    return minIndex;
}


void selectionSort(int arr[], int n)
{
  //code here
  for(int i = 0; i  < n; i++){
      int minIndex = select(arr,i);
      int temp = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
  }
