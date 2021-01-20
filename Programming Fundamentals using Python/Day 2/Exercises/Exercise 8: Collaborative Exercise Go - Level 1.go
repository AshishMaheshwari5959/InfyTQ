///
Write a Go program to calculate and display the final fees to be paid by a student.

The students are entitled to get scholarship based on the marks scored in the qualifying exam. Scholarship percentage should be considered as half of the marks scored by the student on the course fee. Apart from the course fee (after deducting the scholarship amount), the students have to pay an extra service fees.

Consider that course fee, marks scored by the student and extra fees amount are given. Assume that the marks is out of 100 and need not always be integer.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
Course Fee	Marks	Extra Fees	
25000	50	1500	20250
25000	70	1500	
Estimated Time: 20 minutes
///

// Solution

//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var course_fee float32 = 25000
    var marks float32 = 70
    var extra_fees float32 = 1500
    
    finalFee = course_fee - course_fee*marks/200
    finalFee = finalFee + extra_fees


     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
