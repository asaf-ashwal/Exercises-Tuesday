# 1) NameError – accessing a non-existent variable
def greet(username):
    return f"Hello, {username}!"

# print(greet('asaf'))


# 2) Runtime bug
counts = {"a":1, "b":2, "c":3}
new_list = {}
for k in counts:
    if counts[k] % 2 == 1:
        new_list[k] = counts[k]
counts = new_list
# print(counts)



# 3) AttributeError – wrong method/attribute
text = "debugging"
# print(text)



# 4) IndexError – list index out of range
nums = [1, 2, 3]
for i in range(0, len(nums)-1):
    print(nums[(i + 1)])


# 5) KeyError – missing dictionary key
config = {"host": "localhost", "port": 5432}
if "username" in config:
    print(config["username"])
    

# 6) TypeError – adding incompatible types
age = "12"
print(int(age) + 5)


# 7) ValueError – bad int conversion
user_input = "12.5"
print(float(user_input))


# 8) ZeroDivisionError – unchecked divisor
def ratio(a, b):
    if b < 1: 
        return a
    return a / b
# print(ratio(10, 0))


# 9) ImportError / ModuleNotFoundError – misspelled import
import json
print(json.dumps({"ok": True}))


# 10) RecursionError – missing base case
def down(n):
    if n > 0:
        return down(n - 1)
    elif n == 0: 0
print(down(5))


# 11) Infinite loop – loop condition never changes
x = 5
while x > 0:
    print(x)
    x -= 1
# x never changes


# 12) Mutable default argument – state “leaks” across calls
def add_item(item, bucket):
    if type(bucket) != list:
        print('new list is requir')
        return
    bucket.append(item)
    return bucket

# print(add_item("a",{}))
# print(add_item("b",[]))

# Find & fix: Use a safe default pattern.