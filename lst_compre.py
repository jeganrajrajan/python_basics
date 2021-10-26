# for loop
letters = []

for letter in 'human':
    letters.append(letter)

print(letters)
# list_comprehension
letters = [letter for letter in 'human']
print(letters)

# Conditionals in List Comprehension

even_num = [x for x in range(10) if x % 2 == 0]
print(even_num)
even_odd = ["Even" if x % 2 == 0 else "odd" for x in range(100)]
print(even_odd)

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for i in range(2):
#     for row in matrix:
#         print(row[i])
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
# create_list
matrix = [[i for i in range(5)] for _ in range(6)]
# nested list,dictonary
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}

# Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5))

addition = lambda x, y, z: x + y + z
print(addition(5, 6, 2))


# in function
def myfunc(n):
    return lambda a: a * n


doubler = myfunc(2)
print(doubler(11))

# (lambda x,y : x*y)(5,7)
# Define a lambda function that can take another lambda function (func1).
high_order = lambda x, lmbfunc: x*lmbfunc(x)

# The inner lambda function is defined when calling the high_order.
print(high_order(10, lambda x : x*x))

# (lambda *args : sum(args))(3,5,7)

# map()
mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(map(lambda x : x%2, mylist))
print(list_new)

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

# filter()
list_new  = list(filter(lambda x : (x%2==0), mylist))
print(list_new)

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

# reduce()
from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
# print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))