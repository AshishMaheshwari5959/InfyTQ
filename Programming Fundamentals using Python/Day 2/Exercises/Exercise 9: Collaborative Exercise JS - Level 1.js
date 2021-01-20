///
Write a JavaScript program to find and display the number of cookies sold on a day by a shop in the airport.

Assume that the flights which took off are filled to the capacity, flights which landed are half filled and all passengers bought 2 cookies each.

Test your code by using the given sample input.

Sample Input	Expected Output
Flights took off	Flights landed	Seating capacity of flights took off	Seating capacity of flights landed	
100	110	150	185	50350
Estimated Time: 20 minutes
///

// Solution

//PF-Exer-9

noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=0

//Write your code here
//Populate the variable: totalCookies
totalCookies = noOfFlightsTakeOff*seatingCapacityTakeOff*2 + noOfFlightsLanded*seatingCapacityLanded

//Do not modify the below print statement for verification to work
console.log(totalCookies)


