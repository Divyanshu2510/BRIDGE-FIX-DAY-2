# # Q1. Find duplicate elements
# ls=[]
# nums = [10, 20, 20, 30, 40, 40, 50]
# for i in range (len(nums)):
#     for j in range (i+1,len(nums)):
#         if nums[i]==nums[j]:
#             ls.append(nums[i])
# print(ls)
            

# Q2. Find unique elements

# nums = [10, 20, 20, 30, 40, 40, 50]
# ls=[]
# for i in nums:
#     if nums.count(i)==1:
#         ls.append(i)
# print(ls)

# Q3. Reverse a string without using [::-1].

# text = "python"
# rev=""
# for i in text:
#     rev=i+rev
# print(rev)

# name="Divyanshu Kushwah"
# word=name.split()
# for i in word:
#     print(i[::-1],end=" ")



# Q4. Count frequency of each element


nums = [10, 20, 20, 30, 40, 40, 50,20]
freq={}
for i in nums:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)


# Q5. Find the second-largest number

# numbers = [10, 50, 20, 80, 40,80]
# ls=[]
# for i in numbers:
#     if i not in ls:
#         ls.append(i)
# ls.sort()
# print(ls[-2])


# def add(a, b, *numbers):
#     total = a + b

#     for num in numbers:
#         total += num
#         return total
# print(add(2, 3, 4, 5))

# # Q7. Write a function that accepts any number of numbers.
# def add(*agrs):
#     sum=0
#     for i in agrs:
#         sum+=i
#     print(sum)

# add(10, 20, 30, 40)



# Q8. Write a function that returns two values.

# def student(name,age):
#     return name,age
# name,age=student("divyanshu",21)  
# print(name,age)


# class BankAccount:
#     def __init__(self,name,account_num,balance):
#         self.name=name
#         self.account_num=account_num
#         self.balance=balance

#     def deposite(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print("Deposite successfully")

#     def withdraw(self,amount):
#         if self.balance >=amount and amount>0:
#             self.balance-=amount
#             print("withdraw successful")

    

#     def show_balance(self):
#         print(self.balance)

# a=BankAccount("divyasuh",233,200)
# a.deposite(20)
# a.show_balance()

# 🔥 Level 5 — Encapsulation

# # Q11. Create a private balance.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance=balance
#     def get_data(self):
#         return self.__balance

#     def deposite(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print("Deposite successfully")

#     def withdraw(self,amount):
#         if self.__balance >=amount and amount>0:
#             self.__balance-=amount
#             print("withdraw successful")

#     def show_balance(self):
#         print(self.__balance)

# a=BankAccount(2000)
# a.show_balance()
# a.deposite(20)
# a.show_balance()

# 🔥 Level 8 — Advanced Python

# Q15. What is an iterator?

# Create your own iterator that produces:

# # itertor=[1,2,3,4,5,5]
# it=iter([1,2,3,4,5])
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))


# Q16. What is a generator?

# Write:

# def numbers():
#     for i in range(1,100):
#         yield i


# for num in numbers():
#     print(num)



# 💻 Coding Question 4

# Create a Car class with:

# brand
# model
# price

# Use __init__() and create 2 car objects.

# Then print their details.

# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

# c=Car("Motorola","F11","2000")
# print(c.model)


# 💻 Question 5 — Coding

# Create a Student class with:

# Class variable: college = "SVVV"
# Instance variable: name
# Create 2 students: "Divy" and "Rahul"
# Print both names and the college.

# Write the code yourself.

# class Student:
#     collage="SVVV"
#     def __init__(self,name):
#         self.name=name

# s=Student("divy")
# print(s.name)
# print(Student.collage)

# s=Student("rahul")
# print(s.name)
# print(Student.collage)

