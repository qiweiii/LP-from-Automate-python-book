# this is a Automate Boring Stuff in Python practice in Chap 3

def collatz(number):
    if number % 2 == 0:
        print('number / 2 = %s' %(number/2))
        return number/2
    else:
        print('number * 3 + 1 = %s' %(number * 3 + 1))
        return number*3 + 1


print ('Enter number')

userInput = int(input())

print('shit 1')
num = collatz(userInput)

while num != 1:
    num = collatz(num)
