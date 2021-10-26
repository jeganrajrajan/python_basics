# Global variable
x = "global"

def some_func():
    print("x inside:", x)


some_func()
print("x outside:", x)
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()


# Local variable
# def check():
#     y = "local"
#
#
# check()
# print(y)

def foo():
    y = "local"
    print(y)

foo()


# Global&Local variable
x = "global "
def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()


# Nonlocal
def outer():
    x = "local"

    def inner():
        # nonlocal x
        # x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()