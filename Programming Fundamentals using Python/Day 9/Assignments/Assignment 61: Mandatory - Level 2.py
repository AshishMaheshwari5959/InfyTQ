'''
Write a python program to validate the details provided by a user as part of registering to a web application.


Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets


Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number


Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com


All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.
'''

# Solution

#PF-Assgn-61
def validate_name(name):
    if 0 < len(name) <= 15 and name.isalpha():
        return True
    else :
        return False

def validate_phone_no(phno):
    if len(str(phno))==10 and str(phno).isdigit() and len(set(str(phno)))!=1 :
        return True
    else:
        return False

def validate_email_id(email_id):
    if '@' in email_id and '.com' not in email_id[:-3]:
        domain_list=['gmail.com','yahoo.com','hotmail.com']
        temp_list = email_id.split('@')
        if temp_list[1] in domain_list :
            return True
        else : 
            return False
    else :
        return False

def validate_all(name,phone_no,email_id):
    if not validate_name(name) :
        print("Invalid Name")
    elif not validate_phone_no(phone_no):
        print("Invalid phone number")
    elif not validate_email_id(email_id):
        print("Invalid email id")
    else:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
