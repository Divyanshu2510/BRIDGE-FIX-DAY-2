from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class Upi(Payment):
    def pay(self,amount):
        print(f"PAy by the {amount} Upi")

class CreditCArd(Upi):
    def pay(self,amount):
        print(f"Pay by the {amount} CreditCArd")

cred=CreditCArd()
Upi=Upi()
Upi.pay(80)
cred.pay(9000)


