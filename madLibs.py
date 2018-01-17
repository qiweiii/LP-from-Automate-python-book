print('Enter an adjective:')
adj = input()

print('Enter a noun:' )
noun1 = input()

print('Enter a verb')
verb = input()

print('Enter a noun: ')
noun2 = input()

file = open('madlibs.txt', 'w')
file.write('The' + adj + 'panda walked to the' + noun1 + 'and then' + verb + '.A nearby' + noun2 +
      'was unaffected by these events.')

file.close()

output = open('madlibs.txt', 'r')

content = output.read()

output.close()

print(content)
