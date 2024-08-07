class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hey", self.name, "your civil score is :", sum/3)


s1 = student("big B", (15, 20, 4))    
s1.get_avg()

class bank:
    
    def __init__(self):
        self.sutter = False

    def start(self):
        self.sutter = True
        print("machine starts... ")

    def stop(self):
        self.sutter==false
        print("machine stops... ")    

bank1 = bank()
bank1.start()





class Account:
    def __init__(self, bal, acc):
        self.balance= bal
        self.account_no= acc

    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "is debited in your account")

    #cradit
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited in your account")
    


acc1= Account(19000,34567891233)  
acc1.debit (1000)
acc1.credit(500)
acc1.credit(30300)
acc1.debit (5000)
acc1.debit (55)

print(acc1.balance, "is your remaining balance")






class bank:
    
    def __init__(self,type):
        self.type = type
        self.sutter = False

    def start(self):
        self.sutter = True
        print("machine started... ")

    def stop(self):
        self.sutter = False
        print(" machine stoped... ")    

class icic(bank):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name


class icic_branch1(icic):
    def __init__(self,cash):
        self.cash = cash
        
        

bank1 = icic_branch1("cash not avialable",)
bank2 = icic("branch1","AC hall")
print(bank2.type)
print (bank1.cash)
bank1.stop()



 