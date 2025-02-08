class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

acc1= Account(10000,1235)
print(acc1.balance,acc1.account_no)
