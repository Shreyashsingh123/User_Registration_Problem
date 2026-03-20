import re
import pytest


pattern="^[A-Z][A-Za-z]{3,}$"

@pytest.mark.parametrize("first_name,expected",[
  ("Shreyash",True),
    ("Ankur",True),
    ("ayush",False),
    ("Harshit",True),
    ("aditya",False),
    ("An",False)
])

def test_first_name(first_name,expected):
    ans=bool(re.match(pattern,first_name))
    assert ans==expected

@pytest.mark.parametrize("last_name,expected",[
  ("Singh",True),
    ("Verma",True),
    ("abs",False),
    ("sharma1",False),
    ("Sharma",True),
    ("Kumar2",False)
])

def test_last_name(last_name,expected):
    ans=bool(re.match(pattern,last_name))
    assert ans==expected

email_pattern="^[a-zA-Z0-9][a-zA-Z0-9-_+]+(\\.[a-zA-Z0-9-_+]+)*@[a-zA-Z]+(\\.[a-zA-Z0-9]{2,}){1,2}$"

@pytest.mark.parametrize("email,expected",[
  ("abc@yahoo.com",True),
  ("abc-500@yahoo.com",True),
  ("abc..2002@gmail.com",False),
  ("abc@gmail.com.aa.au",False),
  ("abc+100@gmail.com",True),
  (".abdc@gmail.com.aa.au",False),
  ("abc.100@gla.ac.in",True),
  ("Shreyash47@gmail.com",True),
  ("Ayush123_1@gmail.ac.in",True),
  ("abs@.com",False),
  ("abs@gmail.",False)

])

def test_email(email,expected):
    ans=bool(re.match(email_pattern,email))
    assert ans==expected


Phone_pattern="^[0-9]{1,3}\\s[6-9][0-9]{9}$"

@pytest.mark.parametrize("phone,expected",[
    ("91 8574859685",True),
    ("95 8574125241",True),
    ("91251478596",False),
    ("52142563247",False),
    ("63 8887614502",True),
    ("95 6598745847",True),
    ("95 6521452",False),
    ("90 6532145214",True)

])

def test_phone(phone,expected):
    ans=bool(re.match(Phone_pattern,phone))
    assert ans==expected

password_Pattern="^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$^%&_])[a-zA-Z0-9!@#$^%&_]{8,}$"

@pytest.mark.parametrize("password,expected", [
   ("Shreyash1234@", True),
    ("ayush12345@", False),       
    ("Singh@", False), 
    ("ayushman!@", False),
    ("Ayush123Saq",False)


])
def test_password(password, expected):
    result = bool(re.match(password_Pattern,password)) and len(re.findall(r"[!@#$^%&_]", password))==1 
    assert result == expected