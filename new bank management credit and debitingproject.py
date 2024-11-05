import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Bank Class
class Bank:
    def __init__(self):
        self.sutter = False

    def start(self):
        self.sutter = True
        print("Machine starts...")

    def stop(self):
        self.sutter = False
        print("Machine stops...")

# Account Class
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        self.transactions = [balance]  # To keep track of balance changes for animation

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(self.balance)
            print(f"Rs {amount} is debited from your account. Remaining balance: Rs {self.balance}")

    def credit(self, amount):
        self.balance += amount
        self.transactions.append(self.balance)
        print(f"Rs {amount} is credited to your account. New balance: Rs {self.balance}")

# Initialize Bank and Account objects
bank = Bank()
account = Account(19000, 34567891233)

# Start the Bank Machine
bank.start()

# Loop for user input for transactions
while True:
    action = input("Enter 'credit', 'debit' or 'stop' to end transactions: ").lower()
    
    if action == "credit":
        amount = float(input("Enter amount to credit: "))
        account.credit(amount)
    
    elif action == "debit":
        amount = float(input("Enter amount to debit: "))
        account.debit(amount)
    
    elif action == "stop":
        print("Transaction session ended.")
        break
    
    else:
        print("Invalid input. Please enter 'credit', 'debit', or 'stop'.")

# Stop the Bank Machine
bank.stop()

# Animation Code
fig, ax = plt.subplots()
x_data = list(range(len(account.transactions)))
y_data = account.transactions

ax.set_xlim(0, len(x_data) - 1)
ax.set_ylim(0, max(y_data) + 5000)
line, = ax.plot([], [], lw=3, color='blue')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = x_data[:frame + 1]
    y = y_data[:frame + 1]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, interval=500, repeat=False)

plt.title("Bank Account Balance Animation")
plt.xlabel("Transaction Steps")
plt.ylabel("Balance (Rs)")
plt.show()
