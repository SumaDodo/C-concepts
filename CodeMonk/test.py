'''
# Sample code to perform I/O:

name = input()               # Reading input from STDIN
print('Hi, %s.' % name)      # Writing output to STDOUT
'''
number = input()
number = int(number)

for num in range(2, number):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num, end= " ")
