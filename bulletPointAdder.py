
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)


pyperclip.copy(text)


"""
When this program is run,
it replaces the text on the clipboard with text
that has stars at the start of each line. Now the program is complete,
and you can try running it with text copied to the clipboard.
"""
