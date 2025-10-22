# 1. Hello Decorator
def mew_dec(func):
    def wrapper():
        print("Start function")
        func()
        print("End function")
    return wrapper

@mew_dec
def momo():
    print("inner func")
# momo()



# 2. Timing Decorator
import time
def time_dec(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('function run time is:', end - start)
    return wrapper

@time_dec
def momo2():
     for i in range(300):
         pass
     print('momo 2 end')
# momo2()
     
     
     
# 3. Logging Arguments
def logging_arguments(func):
    def wrapper(*args,**kwargs ):
        print(f'- {args}')
        func()
    return wrapper

@logging_arguments
def momo3(*args):
    print('gets all the args')

     
        
# 4. Uppercase Decorator
def uppercase_decorator(func):
    def wrapper(*args):
        return list(map((lambda x : type(x) == str  and x.upper() ) ,args))
    return wrapper
        
@uppercase_decorator
def momo4(*args):
    print('start momo function')

# print(momo4('asaf','or','test'))



# 5. Count Calls
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(count)
    return wrapper

@count_calls
def momo5():
    pass
# momo5()
# momo5()
# momo5()
# momo5()



# 6. Authentication Check
def authentication_check(func):
    def wrapper(**kwargs):
        if kwargs['admin'] == True:
            func()
        else: print('not admin')
    return wrapper

@authentication_check
def momo6(*args,**kwargs):
    print('hii')
momo6(admin = False)