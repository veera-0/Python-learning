

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
    def deposit(self, depositAmount):
        self.balance += depositAmount
        print("Deposit Accepted")

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable")
    
#instantiate the class

acc = Account("Jose", 100)

#print the object
print(acc)

# 3. Show the account owner attribute
print(acc.owner)

# 4. Show the account balance attribute
print(acc.balance)


#5. Make a series of deposits and withdrawals
acc.deposit(50)

acc.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acc.withdraw(500)