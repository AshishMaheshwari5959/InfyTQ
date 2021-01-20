'''
The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. Write a python program to implement the following requirements:

Initialize the following variables with appropriate input values:account_number, account_balance, salary, loan_type, loan_amount_expected and customer_emi_expected.
The account number should be of 4 digits and its first digit should be 1.
The customer should have a minimum balance of Rupees 1 Lakh in the account.
If the above rules are valid, determine the eligible loan amount and the EMI that the bank can provide to its customers based on their salary and the loan type they expect to avail.
The bank would provide the loan, only if the loan amount and the number of EMI’s requested by the customer is less than or equal to the loan amount and the number of EMI’s decided by the bank respectively.
Display appropriate error messages for all invalid data. If all the business rules are satisfied ,then display account number, eligible and requested loan amount and EMI’s.
Test your code by providing different values for the input variables.

Salary	Loan type	Eligible loan amount	No. of EMI’s required to repay
> 25000	Car	500000	36
> 50000	House	6000000	60
> 75000	Business	7500000	84
'''

# Solution

#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected
    if 1000 > account_number or account_number >= 2000 :
        print("Invalid account number")
        return
        
    if account_balance < 100000 :
        print("Insufficient account balance")
        return
    
    if ( loan_type != "Car" and loan_type != "House" and loan_type != "Business" ) or ( loan_type == "Car" and salary <= 25000 ) or ( loan_type == "House" and salary <= 50000 ) or ( loan_type == "Business" and salary <= 75000 ):
        print("Invalid loan type or salary")
        return
    
    if loan_type == "Car" and salary > 25000 :
        eligible_loan_amount = 500000
        bank_emi_expected = 36
    elif loan_type =="House" and salary > 50000 :
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
    elif loan_type =="Business" and salary > 75000 :
        eligible_loan_amount = 	7500000
        bank_emi_expected = 84
    else :
        print("The customer is not eligible for the loan")
        return
    
    if eligible_loan_amount >= loan_amount_expected and bank_emi_expected >= customer_emi_expected :
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)
    else :
        print("The customer is not eligible for the loan")
        return

calculate_loan(1005,20000,255000,"Car",300000,30)
