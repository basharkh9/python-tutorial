# Functions use def keywords
def my_func1():
    print("my first python function")


my_func1()


def my_func2(param1='default'):
    print("my second python function with parameter! {}".format(param1))


my_func2()
my_func2('Ziad')


def my_func3():
    """
    This is the Docstring
    """
    print("my third python function")


my_func3()


def hello():
    return "hello"


result = hello()
print(result)


def addNum(num1, num2):
    return num1+num2


result = addNum(2, 3)
print(type(result))
print(result)

result = addNum("2", "3")
print(type(result))
print(result)


def addNum2(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1+num2
    else:
        return "Sorry I need integers!"


result = addNum2(2, 3)
print(result)

result = addNum2("2", "3")
print(result)

print()

# Lambda Expression

# Example
# Introduce a function that accept another function as parameter
# Filter function

mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
print(list(evens))

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))


# More example
tweet = "Visca Barca! #Football"
result = tweet.split('#')[1]
print(result)

print()

print('x' in [1, 2, 3, 4])

print()

print('x' in [1, 2, 3, 4, 'x'])
