

# #SLOTS
# class A:
#     __slots__=("name","age")

#     def fun(self,name,age):
#         self.name=name
#         self.age=age

# a=A()
# a.fun("divyanshu",22)
# print(a.name)
# a.city="berline"
# print(a.name)
# print(a.age)
# print(a.city)


# __call__

# class A:
#     def __call__(self):
#         print("call by object")

# a=A()
# a()


from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:int
    address:str
    salary:int

s1=Student("divyanshu",21,"82 AS-2 sch no.78",999)
print(s1)

# Dynamic classes

# def init(self,name,age):
#     self.name=name
#     self.age=age

# def show(self):
#     print(self.name,self.age)

# Student=type("student",(),
#           {
#     "__init__":init,
#     "show":show
# })

# s=Student("divy",23)
# print(s.show())
