# list

list_val = ["apple", "banana", "cherry", "apple", "cherry"]
print(list_val)
# len
print(len(list_val))
list1 = ["abc", 34, True, 40, "male"]

# type()
list1.append('orange')
print(list1)
list2 = [1,3,78,7,4,1,78]
print(list2.count(78))
list1.append(list2)
print(list1)
# list2.clear()
list3 = list1.copy()
print(list3)
fruits = ['apple', 'banana', 'cherry']

cars = ('Ford', 'BMW', 'Volvo','volvo')
fruits.extend(cars)
print(fruits)
# list.extend(list, set, tuple,etc..,)
print(cars.index('BMW'))
# list.insert(pos, elmnt)
fruits.insert(1,6)
print(fruits)
fruits1 = ['apple', 'banana', 'cherry']
fruits1.pop(1)
print(fruits1)
fruits1.remove('apple')
print(fruits1)
# list1.reverse()  reverse the order of the list
# cars.sort(reverse=True) it will sort the list by default asending


#TUPLES
t = (5,'program', 1+3j)
# t[1] = 'program'
print("t[1] = ", t[1])

tuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = tuple1.count(5)
y = tuple1.index(8)
print(y)

#set
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# fruits.clear()
y = fruits.copy()
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
z = x1.difference(y1)
x1.difference_update(y1)
# x1.pop()  removes random item from the list
# x1.remove()  removes specific elemen from the list

fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}

fruits.update(company)
print(fruits)

# string
txt = "hello, and welcome to my world hello."
x = txt.capitalize()
txt.casefold()
txt.count("apple")
# txt.endswith(".") check the statement True or False
dicto ={80:30}
x = 'good'
x.translate(dicto)
# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))

txt = "Hello Sam!"

mytable = txt.maketrans("S", "P")

print(txt.translate(mytable))

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))

# Dictonary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)
# x = car.copy()
x_key = ('key1', 'key2', 'key3')
y_val = 0

newdict = dict.fromkeys(x_key, y_val)

print(newdict)
get_val = car.get("model")
get_item = car.items()
car.pop('model')
car.popitem()
car.update({"color": "White"})
