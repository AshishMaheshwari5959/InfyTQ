///
Write a JavaScript program to find and display least common multiple of two whole numbers.
Least Common Multiple of two numbers, say num1 and num2, is the smallest positive number that is divisible by both num1 and num2.
Note: Initialize the numbers with various values and test your program.

Test your code by using the given sample input.
Sample Input	Expected Output
Num1	Num2	
5	10	10
///

// Solution

//PF-Exer-16

num1=5
num2=10

//Write your code here
flag = 0
num = 1
while (flag == 0){
    if (num%num1 == 0  && num%num2 == 0){
        break
    }
    else{
        num = num + 1
    }
}

console.log(num)
