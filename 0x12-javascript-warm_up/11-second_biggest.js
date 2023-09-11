#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log('0');
} else {
  let sortedArray = [];
  for (let i = 2; i < len; i++) {
    const num = parseInt(process.argv[i]);
    sortedArray = insertSort(sortedArray, num);
  }
  console.log(sortedArray[sortedArray.length - 2]);
}
function insertSort (arr, num) {
  const SortedArr = [...arr];
  if (!SortedArr) {
    SortedArr[0] = num;
    return arr;
  }

  let i = arr.length - 1;
  while (i >= 0 && SortedArr[i] > num) {
    SortedArr[i + 1] = SortedArr[i];
    i--;
  }
  SortedArr[i + 1] = num;
  return SortedArr;
}
