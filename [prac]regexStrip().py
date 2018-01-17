

'''
Write a function that takes a string and
does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed
from the beginning and end of the string.
Otherwise, the characters specified in the second argument
to the function will be removed from the string.
'''


import re

def regexStrip(txt,arg=''): # assigning a default value to arg prevents the error if no argument is passed when calling strippp()
    if arg =='':
        regex1 = re.compile(r'^(\s+)')
        mo = regex1.sub('', txt)
        regex2 = re.compile(r'(\s+)$')
        mo = regex2.sub('', mo)
        print(mo)
    else:
        regex1 = re.compile(arg)
        mo = regex1.sub('', txt)
        print(mo)

text = '        So, you can create the illusion of smooth motion        '
regexStrip(text, 'e')
regexStrip(text)
