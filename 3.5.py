x = int(input("Enter number of repetitions"))
def my_decorator(func):
    def wrapper():
        for i in range(x):
           func()
    return wrapper

@my_decorator
def hello():
    print("hello")

hello()