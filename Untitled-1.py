class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hey", self.name, "your avg score is :", sum/3)


s1 = student("big B", (15, 20, 4))    
s1.get_avg()






class car:
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = car()
car1.start()



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