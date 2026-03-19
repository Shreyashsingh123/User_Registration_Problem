# User registration problem
import re
class User:
    def __init__(self,First_name,last_name):
        self.First_name=First_name
        self.last_name=last_name
    def __str__(self):
        return f"{self.First_name} {self.last_name}"

def is_Valid_first_name(first_name):
    try:
        pattern="^[A-Z][A-Za-z]{3,}$"
        match=re.match(pattern,first_name)
        if not match:
            raise ValueError("! First name should start with upper case and length must be greater than 3")
        return True
    except ValueError as e:
        print(e)

def is_Valid_last_name(last_name):
    try:
        pattern="^[A-Z][A-Za-z]{3,}$"
        match=re.match(pattern,last_name)
        if not match:
            raise ValueError("! Last name should start with upper case and length must be greater than 3")
        return True
    except ValueError as e:
        print(e)

def main():
    while(True):
        first_name=input("Enter first name: ")
        last_name=input("Enter last name")
        valid_first=is_Valid_first_name(first_name)
        valid_last=is_Valid_last_name(last_name)
        if valid_first==True and valid_last==True:
            user1=User(first_name,last_name)
            print(user1)
            # return

if __name__=="__main__":
    main()

        
