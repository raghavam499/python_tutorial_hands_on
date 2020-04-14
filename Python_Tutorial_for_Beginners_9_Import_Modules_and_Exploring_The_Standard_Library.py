#from corey schafer tutorials - 8

def hello_fun():
    return "Hello Function."

print(hello_fun())
def hello_fun(greeting):
    return "{} Function".format(greeting)

print(hello_fun('Hi'))
def hello_fun(greeting, name="You"):
    return "{}, {} Function".format(greeting,name)

print(hello_fun('Hi',"raghava"))
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("slice","quadrillion",type='finance', card='physical')
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Maths', 'Art']
info = {'name':'John', 'age':22}
student_info(*courses, **info)
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year%4 == 0:
        if year%100 != 0 or year%400 == 0:
                return True
        else:
            return False
    else:
        return False

def days_in_month(year, month):
    if not 1<=month<=12:
        return "invalid month"
    if month == 2 and is_leap(year):
        return 29
    return days_in_month[month]

print(is_leap(2016))
