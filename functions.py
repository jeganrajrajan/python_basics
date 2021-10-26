# Python Creating Function

def greet():
    a = "welcome" + "computer vison programme"
    print(a)
    return a
greet()


# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(20)


# keyword arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='computer', lastname='vision')
student(lastname='Practice', firstname='python')


# *args for variable number of arguments
def myFun(*args):
    for arg in args:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# *kargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='ram', mid='for', last='ram')


