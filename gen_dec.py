# ---------------------------Example 1 -------------------------------------------
# simple Generator
def simple_generator():
    num = 0
    while num < 3:
        yield num
        num += 1


# iterator = simple_generator()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


for i in simple_generator():
    print(i)
# Example 2
# generator with multilpe
print('\n'*2, 'Example 2\n', sep='')

def generator2():
    num = 1
    # Generator function contains yield statements
    yield num

    num += 1
    yield num

    num += 1
    yield num


# Using for loop
for item in generator2():
    print(item)

# Example of python generator expression

lst = [1,2,3,4]

# this generator will square all the number of the list
generator = (x**2 for x in lst)

# let's iterate through the generator
for item in generator:
  print(item)

# decorator

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(1,2)

# chaining decorator in python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hi")
