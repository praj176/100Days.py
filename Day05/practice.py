#For loop

# fruits = ['apple','grapes', 'orange', 'banana']
# for fruit in fruits:
#     print(fruit)

# using for function to replicate the functionality of sum built-in function in python

# list = [1,2,3,4,5]
# sum = 0
# for item in list:
#     sum+=item
    
# print(sum)

##########
# Using for loop for MAX functionality
##########

# list = [1,2,3,4,5]

# max = 0
# for item in list:
#     if item > max:
#         max = item
        
# print(max)

###################3
# For function for printing 1-10 numbers

# for number in range(1,11):
#     print(number)
    
#################
# Gaus challenge for the sum of all the numbers from 1-100

# sum = 0
# for i in range(1,101):
#     sum += i
    
# print(sum)

##############################################3
#Fizzbuzz

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num%5 ==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print(num)
