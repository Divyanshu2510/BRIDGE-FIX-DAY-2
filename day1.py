# # ENCAPSULATION GET AND SET METHOD
# class Person:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
    
#     def set_balance(self,balance):
#         self.__balance=balance

#     def deposite(self,amount):
#         if amount >0:
#             self.__balance+=amount
#         else:
#             print("enter positive amount")
    
#     def withdraw(self,amount):
#         if amount>0 and amount<=self.__balance:
#             self.__balance-=amount

#         else:
#             print("invalid amount")

#     def get_data(self):
#         return self.__balance

    
# p=Person("Divyanshu",2000)
# p.set_balance(7000)
# p.deposite(1000)
# p.withdraw(2000)
# print(p.get_data())

# def add(a,b):
#     return a+b

# # OVERLOADING
# def add(a,b,*numbers):
#     total=a+b
#     for number in numbers:
#         total+=number
#     return total
    
# print(add(2,4))
# print(add(2,3,4))



# #CLASS METHOD

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class BankAccount(Person):
#     bank="SBI"
#     def __init__(self,name,age,account_no):
#         super().__init__(name,age)
#     @classmethod
#     def change_bank(cls,new_bank):
#         cls.bank=new_bank

# class ICICBank(BankAccount):
#     pass

# class HDFCBank(ICICBank):
#     pass

# HDFCBank.change_bank("HDFC")
# ICICBank.change_bank("ICIC")
# print(BankAccount.bank)
# print(HDFCBank.bank)
# print(ICICBank.bank)

        