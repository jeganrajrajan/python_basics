import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


# Finally
# try:
#    f = open("test.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()


# zip()
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)


# Unzipping the Value Using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)

# join

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

# any()
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))


# all():
print(all([2 == 2, 3 == 2]))
print(all([2 > 1, 3 != 4]))
print(all([True, False, False]))
print(all([False, False]))







# old_list = ["just", "Some", "text", "As", "An", "example"]
# list_begins_upper = list(map(lambda x: x[0].isupper(), old_list))
# list_shorter_than_8 = [len(x) < 8 for x in old_list]
#
# print(list_begins_upper)
# print(list_shorter_than_8)
#
# print("Do all the strings begin with an uppercase letter? " + str(all(list_begins_upper)))
# print("Are all the strings shorter than 8? " + str(all(list_shorter_than_8)))