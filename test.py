
def power(n):
    def bla():
        return  n*n 
    return bla
# var = power(4)
# print(var())


def main():
    count = 0
    def inner ():
        nonlocal count
        count += 1
        return count
    return inner
# x = main()
# x()
# x()
# x()
# print(x())