#！python3

# Table Printer

"""
* Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

'''
Output:
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

def printTable(table):
    colWidths = [0] * len(table) # 3 items
    # find the largest string in each column and make it the width for that colomn
    for i in range(len(table)):
        colWidths[i] = max(table[i], key = len) # I googled this

    # now, colWidths has the largest string in each item in table
        
    for index in range(len(table[0])): # 4 loops
        for i in range(len(table)): # 3 loops
            print(table[i][index].rjust(len(colWidths[i])), end = ' ')

        print('\n')

printTable (tableData)
