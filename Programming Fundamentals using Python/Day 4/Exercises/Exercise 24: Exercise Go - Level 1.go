/*
Write a Go function, find_square() that accepts an integer number, n and returns the square of n.
Invoke the function and display the square of the number.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
5	25
3	
*/

// Solution

/*PF-Exer-24
This verification is based on string match.
*/
package main

//import ("fmt")
func find_square(num int) (int) {
    return (num*num)  
}
func main() {
    //Write your program logic here
    function_call:=find_square(3)
    print(function_call)
}
