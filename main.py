import math
import my_module as mm
import datetime as dt
x = int(input("Enter the number"))
try:
    y = math.sqrt(x)
    print(f"The square root of {x} is ",y)
except TypeError:
    print('Please enter a number, not a string')
except ValueError:
    print('Please enter a non negative number')

myList = []
size=int(input("Enter the size of the list"))
for i in range(size):
    x = int(input("Enter the {}th element".format(i+1)))
    myList.append(x)






mm.getSum(myList)
mm.getMax(myList)
mm.getAverage(myList)

import Calculator

num1 = 10
num2 = 5

print("Addition:", Calculator.addition(num1, num2))
print("Subtraction:", Calculator.subtraction(num1, num2))
print("Multiplication:", Calculator.multiplication(num1, num2))
print("Division:", Calculator.division(num1, num2))


current_datetime = dt.datetime.now()
print("Current Date and Time:", current_datetime)


import data_processing

given_list = [5, 2, 7, 1, 9]


print("Ascending Order:", data_processing.sort_list(given_list, "asce"))

print("Descending Order:", data_processing.sort_list(given_list, "desc"))

import statistics
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
