#! python3


# The .pyw extension means that Python won’t show a Terminal
# window when it runs this program

# The program will save each piece of clipboard text under a keyword.
# For example, when you run py mcb.pyw save spam,
# the current contents of the clipboard will be saved with the keyword spam.
# This text can later be loaded to the clipboard again by running
# py mcb.pyw spam.
# And if the user forgets what keywords they have,
# they can run py mcb.pyw list to
# copy a list of all keywords to the clipboard.

'''
Here’s what the program does:

    The command line argument for the keyword is checked.

    If the argument is save, then the clipboard contents are saved to the keyword.

    If the argument is list, then all the keywords are copied to the clipboard.

    Otherwise, the text for the keyword is copied to the clipboard.

This means the code will need to do the following:

    Read the command line arguments from sys.argv.

    Read and write to the clipboard.

    Save and load to a shelf file.
'''

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword>- delete a key wor from the shelf
#        py.exe mcb.pyw delete - delete all keywords

import shelve, pyperclip, sys
# Whenever the user wants to save a new piece of clipboard text,
# you’ll save it to a shelf file.
# Then, when the user wants to paste the text back to their clipboard,
# you’ll open the shelf file and load it back into your program.
# The shelf file will be named with the prefix mcb 

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
    '''
    the second command line argument is the keyword for the current content of the clipboard.
    The keyword will be used as the key for mcbShelf,
    and the value will be the text currently on the clipboard
    '''

elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for i in mcbShelf:
            del mcbShelf[sys.argv[i]]


        
mcbShelf.close()
