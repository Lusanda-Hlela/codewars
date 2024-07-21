function highAndLow(numbers) {
  let arr = numbers.split(' ');
  var newArr = [];
  for (let i = 0; i < arr.length; i++) {
    num = parseFloat(arr[i]);
    newArr = newArr.concat(num);
  }
  // Function sorts two arguments using the elements of each argument or item within a an array
  newArr.sort(compareFun);

  function compareFun(a, b) {
    return a - b;
  }
  return `${newArr[newArr.length -1]} ${newArr[0]}`;
}