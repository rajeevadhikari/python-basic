# Given a list of integers, [1, 2, 3, 4, 5], use map to create a new list where each element is squared.
# numbers = [1,2,3,4,5,6]
# def square(x):
#         return x**2
# squares = list(map(square, numbers))
# print(str(squares)) 


# using lambda
# numbers = [1, 2, 3, 4, 5]
# # Use map to square each element
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)



# From the list [10, 15, 20, 25, 30], use filter to get a new list containing only numbers divisible by 10.
# numbers = [10, 15, 20, 25, 30]
# def division(x):
#     return x % 10 == 0
# divide_by = list(filter(division, numbers))
# print(divide_by)

# using lambda
# numbers = [10, 15, 20, 25, 30]
# divisible_by_10 = list(filter(lambda x: x % 10 == 0, numbers))
# print(divisible_by_10)


# Use reduce to calculate the product of all numbers in the list [1, 2, 3, 4, 5].
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x,y):
    return x * y 
add = int(reduce(multiply, numbers))
print(add)


