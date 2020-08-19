// https://www.codewars.com/kata/552c028c030765286c00007d/solutions/javascript

const iqTest = (numbers) => {
  numAry  = numbers.split(" ");
  evens = [];
  odds = [];
  numAry.forEach((num, index) => {
    if (num % 2 === 0) {
      evens.push(num) 
    } else {
      odds.push(num)
    }
  })
  return numAry.indexOf(
    evens.length === 1 ? evens[0] : odds[0]
  ) + 1
}
