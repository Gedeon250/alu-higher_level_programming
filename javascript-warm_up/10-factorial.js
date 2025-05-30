#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || (a <= 0)) {
    return 1;
  } else {
    // using recursive way of finding factorial of number
    return a * factorial(a - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
