/*
Write a Java Script function, find_sum() that accepts an integer, n and returns the sum of first, n numbers.
Invoke the function and display the sum of first n numbers.

Test your code by using the given sample input.
Sample Input	Expected Output
6	21

*/

// Solution

//JS-Exer-25

//Start writing your code here
function find_sum(n){
    if (n>0){
        sum = sum + n;
        n = n - 1 ;
        find_sum(n);
    }
    else {
        console.log(sum);
        return sum;
    }
}
sum=0
find_sum(6)
