# User registration problem
import re
class User:
    def __init__(self,First_name,last_name,email,phone,password):
        self.First_name=First_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.password=password
    def __str__(self):
        return f"User Details are:\nFirst Name:{self.First_name}\nLast Name:{self.last_name}\nEmail:{self.email}\nPhone number:{self.phone}\nPassword:{self.password}"

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
    Validation of a Email Address as
    it should follow all condition 
    '''
    try:
        pattern="^[a-zA-Z0-9][a-zA-Z0-9-_+]+(\\.[a-zA-Z0-9-_+]+)*@[a-zA-Z]+(\\.[a-zA-Z0-9]{2,}){1,2}$"
        match=re.match(pattern,email)
        if not match:
            raise ValueError ("! Invalid Email ")
        return True
    except ValueError as e:
        print(e)
def is_Valid_Phone(phone):
    '''
    Validate the phone number of password that it should start with 
    country code followed by space and then phone number 
    '''
    try:
        pattern="^[0-9]{1,3}\s[6-9][0-9]{9}$"
        match=re.match(pattern,phone)
        if not match:
            raise ValueError ("! Invalid Phone number format ")
        return True
    except ValueError as e:
        print(e)
def is_valid_password(password):
    '''
    Validate the password of user that it should be of length 8 and 
    it should have at least one upper case letter and one numeric number should
    be there and also only one special character should be there
    '''
    try:
        pattern="^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$^%&_])[a-zA-Z0-9!@#$%^&_]{8,}$"
        match=re.match(pattern,password)
        if not match:
            raise ValueError ("! Invalid Password format ")
        if match and len(re.findall(r"[!@#$^%&_]",password))==1:
            return True
        else:
            raise ValueError ("! Invalid Password format ")

    except ValueError as e:
        print(e)

def main():
    while(True):
        first_name=input("Enter first name: ")
        last_name=input("Enter last name")
        email=input("Enyter email address:")
        phone=input("Enter your phone number:" )
        password=input("Enter Password:")
        valid_first=is_Valid_first_name(first_name)
        valid_last=is_Valid_last_name(last_name)
        valid_email=is_valid_email(email)
        valid_phone=is_Valid_Phone(phone)
        valid_password=is_valid_password(password)
        if valid_first==True and valid_last==True and valid_email==True and valid_phone==True and valid_password==True:
            user1=User(first_name,last_name,email,phone,password)
            print(user1)
            # return

if __name__=="__main__":
    main()

        
