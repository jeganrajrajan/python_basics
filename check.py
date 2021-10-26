def my_deco(func):
    def wrapper(*args,**kwargs):
        print('start call')
        result = func(*args,**kwargs)
        print('end call')
        return result
    return wrapper

@my_deco
def add(a,b):
    addition = a+b
    print('sum of the numbers:',addition)
    return addition

add(2,7)
