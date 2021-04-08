from datetime import*
class bank:
    bank_name="sbi"

    def __init__(self,acno,c_name,phno,balance,bank_name):
        self.acno = acno
        self.c_name = c_name
        self.phno =phno
        self.balance=balance

    def deposit (self,amount):
        self.balance+=amount
        print("a/n noxxxx",self.acno,"credited with",amount,"on",datetime.today(),"your available balance is",self.balance,"in",self.bank_name)

    def withdraw(self,amount):
        if amount >self.balance:
            print("trasaction is fail")
        else:
            self.balance-=amount
            print("acno",self.acno,"debited with",amount,"on",datetime.today(),"your available balance is",self.balance,"in",self.bank_name)

    def balance_enquiry(self):
        print("your available balance is",self.balance)

obj=bank(100125578649560, "karthika",9946032487,7000,"sbi")
obj.deposit(500)
obj.withdraw(1800)