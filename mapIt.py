#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
# C:\> mapit 870 Valencia St, San Francisco, CA 94110

# other things to do with webbrowser :
# Open all links on a page in separate browser tabs.

# Open the browser to the URL for your local weather.

# Open several social network sites that you regularly check.

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    '''
    ... the sys.argv variable will contain this list value:
    ['madpIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']
    '''
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


'''
Manually getting a map

Highlight the address.

Copy the address.

Open the web browser.

Go to http://maps.google.com/.

Click the address text field.
 
Paste the address.
 
Press ENTER.
 
See how mapIt.py makes this task less tedious?
'''
