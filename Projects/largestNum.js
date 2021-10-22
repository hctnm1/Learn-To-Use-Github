function largestOfFour(arr) {
  let array = [];
  for (let i=0;i<arr.length;i++){
    let larg = arr[i][0];
    for(let j =0;j<arr[i].length;j++){
      if (arr[i][j] > larg){
        larg = arr[i][j];
      }
    }
    array[i] = larg;
  }
  return array;
}
