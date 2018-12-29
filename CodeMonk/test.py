'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
number = input()
number = int(number)

for num in range(2, number):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num, end= " ")
