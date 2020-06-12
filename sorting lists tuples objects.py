>>> li = [4,294,21,44,25,1,3,6]
>>> sort_list = sorted(li)
>>> print(li)
>>> print(sor_list)
>>> li.sort()
>>> print(li)
>>> li.sort(reverse=True)
>>> print(li)

>>> tup = (542, 294, 44, 25, 22, 21, 6, 4, 3, 1)
>>> s_tup = sorted(tup)
>>> print(s_tup)

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '{},{},{}'.format(self.name,self.age,self.salary)
from operator import attrgetter

e1 = Employee('Carl',22,70000)
e2 = Employee('Sarah',25, 80000)
e3 = Employee('Raghava',27, 90000)

employees = [e1,e2,e3]


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees,key=e_sort)
#s_employees = sorted(employees,key=lambda e:e.name,reverse=True)
#s_employees = sorted(employees,key=attrgetter('name'),reverse=True)
print(s_employees)
