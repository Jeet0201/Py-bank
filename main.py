class Account:

    def __init__(self,bal,acc):
        self.balance=bal
        self.account_num=acc

    def debited(self,ammount):
        self.balance-=ammount
        print("Rs.",ammount,"was debited")
        print("total balance is=",self.get_balance())

    def credited(self,ammount):
        self.balance+=ammount
        print("Rs.",ammount,"was debited")
        print("total balance is=",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,"xxxx4587")
acc1.debited(1000)
acc1.credited(500)