import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
X = [ 15, 12, 8,  8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

sum_x, sum_y, numerator, b, c= 0, 0, 0, 0, 0

for i in range(len(X)):
    sum_x,sum_y = sum_x+X[i], sum_y+Y[i]

mean_x = float(sum_x)/len(X)
mean_y = float(sum_y)/len(Y)

for i in range(len(X)):
    numerator += (X[i]-mean_x)*(Y[i]-mean_y)
    b += (X[i]-mean_x)**2
    c += (Y[i]-mean_y)**2

result = float(numerator)/math.sqrt(b*c)
print(result) 
