function descendingOrder(n){
   let num = n.toString();
   let arr = num.split('');
   arr.sort().reverse();
   let toNum = arr.join("");
   return parseInt(toNum);
}