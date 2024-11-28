## pervious work



# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Bank Class with animation properties
# class Bank:
#     def __init__(self):
#         self.sutter = False

#     def start(self):
#         self.sutter = True
#         print("Machine starts... ")

#     def stop(self):
#         self.sutter = False
#         print("Machine stops... ")

# # Account Class
# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no
#         self.balance_history = [balance]  # Track balance changes for animation

#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= amount
#             self.balance_history.append(self.balance)
#             print(f"Rs {amount} is debited from your account. Current balance: Rs {self.balance}")

#     def credit(self, amount):
#         self.balance += amount
#         self.balance_history.append(self.balance)
#         print(f"Rs {amount} is credited to your account. Current balance: Rs {self.balance}")

# # Initialize Bank and Account objects
# bank = Bank()
# account = Account(19000, 34567891233)

# # Start Machine
# bank.start()

# # User transactions
# while True:
#     action = input("\nEnter 'd' to debit, 'c' to credit, or 'q' to quit: ").lower()
#     if action == 'q':
#         print("Exiting the transaction system.")
#         break
#     elif action in ('d', 'c'):
#         try:
#             amount = int(input("Enter the amount: "))
#             if amount <= 0:
#                 print("Amount must be greater than zero. Try again.")
#                 continue
#             if action == 'd':
#                 account.debit(amount)
#             elif action == 'c':
#                 account.credit(amount)
#         except ValueError:
#             print("Invalid input. Please enter a valid amount.")
#     else:
#         print("Invalid option. Please choose 'd', 'c', or 'q'.")

# # Stop Machine
# bank.stop()

# # Animation Code
# fig, ax = plt.subplots()
# x_data = list(range(len(account.balance_history)))
# ax.set_xlim(0, len(x_data) - 1)
# ax.set_ylim(0, max(account.balance_history) + 5000)
# line, = ax.plot([], [], lw=3, color='blue')

# def init():
#     line.set_data([], [])
#     return line,

# def update(frame):
#     x = x_data[:frame + 1]
#     y = account.balance_history[:frame + 1]
#     line.set_data(x, y)
#     return line,

# ani = FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, interval=500, repeat=False)

# plt.title("Bank Account Balance Animation")
# plt.xlabel("Transaction Steps")
# plt.ylabel("Balance (Rs)")
# plt.show()


## new
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# Account Class
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        self.balance_history = [balance]  # Track balance changes for animation

    def debit(self, amount):
        if amount > self.balance:
            return False, "Insufficient balance."
        else:
            self.balance -= amount
            self.balance_history.append(self.balance)
            return True, f"Rs {amount} is debited. Current balance: Rs {self.balance}"

    def credit(self, amount):
        self.balance += amount
        self.balance_history.append(self.balance)
        return True, f"Rs {amount} is credited. Current balance: Rs {self.balance}"

# GUI Application Class
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account GUI")
        self.account = Account(19000, 34567891233)
        
        # Create UI Elements
        self.balance_label = tk.Label(root, text=f"Current Balance: Rs {self.account.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.entry_label = tk.Label(root, text="Enter Amount:", font=("Arial", 12))
        self.entry_label.pack(pady=5)
        self.amount_entry = tk.Entry(root, font=("Arial", 12), width=20)
        self.amount_entry.pack(pady=5)

        self.debit_button = tk.Button(root, text="Debit", command=self.debit_amount, font=("Arial", 12), bg="red", fg="white")
        self.debit_button.pack(pady=5)

        self.credit_button = tk.Button(root, text="Credit", command=self.credit_amount, font=("Arial", 12), bg="green", fg="white")
        self.credit_button.pack(pady=5)

        self.animate_button = tk.Button(root, text="Show Animation", command=self.show_animation, font=("Arial", 12))
        self.animate_button.pack(pady=10)

        # Message box for operations
        self.message_box = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.message_box.pack(pady=10)

    def debit_amount(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            success, message = self.account.debit(amount)
            if not success:
                messagebox.showerror("Error", message)
            else:
                self.update_balance_label()
                self.message_box.config(text=message)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def credit_amount(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            success, message = self.account.credit(amount)
            self.update_balance_label()
            self.message_box.config(text=message)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def update_balance_label(self):
        self.balance_label.config(text=f"Current Balance: Rs {self.account.balance}")

    def show_animation(self):
        # Create a new window for animation
        anim_window = tk.Toplevel(self.root)
        anim_window.title("Account Balance Animation")
        fig, ax = plt.subplots()
        
        # Plot settings
        x_data = list(range(len(self.account.balance_history)))
        ax.set_xlim(0, len(x_data) - 1)
        ax.set_ylim(0, max(self.account.balance_history) + 5000)
        line, = ax.plot([], [], lw=3, color='blue')

        def init():
            line.set_data([], [])
            return line,

        def update(frame):
            x = x_data[:frame + 1]
            y = self.account.balance_history[:frame + 1]
            line.set_data(x, y)
            return line,

        ani = FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, interval=500, repeat=False)
        plt.title("Bank Account Balance Animation")
        plt.xlabel("Transaction Steps")
        plt.ylabel("Balance (Rs)")

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=anim_window)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
