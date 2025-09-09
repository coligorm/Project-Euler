/*
Multiples of 3 or 5
 
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Ans: 233168
*/
let test = 10;
let input = 1000;

function mul_of_3_or_5(params) {
    if (params % 5 == 0 || params % 3 == 0) {
        return true;
    } else {
        return false;
    }
    
}

let count = 0
for (let index = 1; index < input; index++) {
    if (mul_of_3_or_5(index)) {
        count += index;
    }
}

console.log("The sum of all multiples of 3 and 5 below " + input + " is " + count);