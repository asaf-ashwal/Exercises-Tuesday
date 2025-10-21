# 1) Local vs Global (5 דק)
x = 10

def show():
    x = 5
    print("Inside:", x)
    return x

# x = show()
# print("Outside:", x)
# המשתנים לא אותו דבר כי אחד פנימי והשני חיצוני


# 2) Using global (5 דק)
count = 0

def add():
    global count
    count += 1
    print(count)

# add()
# נכשל כי ניסת לשנות משתנה שמחוץ לפונקציה בלי להגדיר אותו גלובלי


# 3) Nested Scope (LEGB) (5 דק)
msg = 'hi'
def outer():
    msg = "Hello"
    def inner():
        print(msg)
    inner()

# outer()
# ההודעה מגיעה מהפונקצייה הפנימית בגלל שאני מפעיל את הפונקצייה החיצונת היא מדליקה את הפנימית


# 4) Using nonlocal (5 דק)
def counter():
    num = 0
    def add_one():
        nonlocal num
        num += 1
        print(num)
    add_one()

# counter()
# הבעיה היא דשהוא מנסה לשנות משתנה שלא נמצא בתוך בפונקצייה וגלובל לא יעזור כי הוא לא נחשב גלובל כי זה פונקצייה בתוך פונקצייה 



# 5) Scope Shadowing (5 דק)
name = "Tom"

def greet():
    name = "Ben"
    print("Hi", name)

# name = greet()
# print("Bye", name)



# פיסקה 2



#1) Basic Closure (5 דק)
def make_greeter(name):
    def greet():
        print('hii',name)
    return greet
say_hi = make_greeter('Dudu')
say_hi()
# הפונקציה הראשונה מעבירה לSAY_HI פונקציה עם השם DUDU והוא תמיד זוכר אותה ואז שאני מפעיל את SAY_HI אני אומר לפונקצייה עם DUDU להדלק


#2)  Discount Factory (10 דק)
