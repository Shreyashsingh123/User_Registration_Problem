# User registration problem
import re
class User:
    def __init__(self,First_name,last_name,email,phone):
        self.First_name=First_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
    def __str__(self):
        return f"First Name:{self.First_name}\nLast Name:{self.last_name}\nEmail:{self.email}\nPhone number:{self.phone}"

def is_Valid_first_name(first_name):
    '''
    Validate First name of user as per condition
    '''
    try:
        pattern="^[A-Z][A-Za-z]{3,}$"
        match=re.match(pattern,first_name)
        if not match:
            raise ValueError("! First name should start with upper case and length must be greater than 3")
        return True
    except ValueError as e:
        print(e)

def is_Valid_last_name(last_name):
    '''
    Validate last name of user 
    '''
    
    try:
        pattern="^[A-Z][A-Za-z]{3,}$"
        match=re.match(pattern,last_name)
        if not match:
            raise ValueError("! Last name should start with upper case and length must be greater than 3")
        return True
    except ValueError as e:
        print(e)

def is_valid_email(email):
    '''
    Validation of a basic Email Address
    '''
    try:
        pattern="^[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+$"
        match=re.match(pattern,email)
        if not match:
            raise ValueError ("! Invalid Email ")
        return True
    except ValueError as e:
        print(e)
def is_Valid_Phone(phone):
    try:
        pattern="^[0-9]{1,3}\s[6-9][0-9]{9}$"
        match=re.match(pattern,phone)
        if not match:
            raise ValueError ("! Invalid Phone number format ")
        return True
    except ValueError as e:
        print(e)
def main():
    while(True):
        first_name=input("Enter first name: ")
        last_name=input("Enter last name")
        email=input("Enyter email address:")
        phone=input("Enter your phone number:" )
        valid_first=is_Valid_first_name(first_name)
        valid_last=is_Valid_last_name(last_name)
        valid_email=is_valid_email(email)
        valid_phone=is_Valid_Phone(phone)
        if valid_first==True and valid_last==True and valid_email==True and valid_phone==True:
            user1=User(first_name,last_name,email,phone)
            print(user1)
            # return

if __name__=="__main__":
    main()

        
