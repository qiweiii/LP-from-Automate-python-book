#! python3

'''
Write a function that uses regular expressions to make sure
the password string it is passed is strong.
A strong password is defined as:
one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.
'''
# crtl + c your password and run this program
import re, pyperclip



# create a regex obj, I will use groups so later can tell which pattern
# is not followed
pwLength = re.compile(r'.{8,}')            # length >= 8   )
pwUpper = re.compile (r'([A-Z]{1,8})')        # at least 1 upper character,
pwLower = re.compile(r'[a-z]{1,}')   # at least 1 lowercase char
pwSpecial = re.compile(r'[^a-zA-Z0-9]{1,}')  # at least 1 special character


# Find match
# check match, and ask user to modify
password = pyperclip.paste()
print(password)

length = pwLength.search(password)
upper = pwUpper.search(password)
lower = pwLower.search(password)
special = pwSpecial.search(password)

if length == None:
    print('your password needs to be at least 8 characters long, pls modify')
elif upper == None:
    print('your password needs to contain at least 1 uppercase letter, pls modify')
elif lower == None:
    print('your password needs to contain at least 1 lowercase letter, pls modify')
elif special == None:
    print('your password needs to contain at least 1 special character, pls modify')
else:
    print('Your password is strong')




