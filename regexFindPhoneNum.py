import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Creating Regex Objects
mo = phoneNumRegex.search('My number is 415-555-4242.') # returns a match Objects
print('Phone number found: ' + mo.group()) # match objects have a group method that returns actual matched text
