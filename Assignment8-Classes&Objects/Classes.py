
'''
Problem 1:
Create a class called Person having 
attributes as 
Name
Age
Methods as 
__init__()
Birthday()
isteenager()
__init__ method should initilise the values for Name and Age
Birthday Method should take age as input parameter and it should display “Happy birthday Message” 
and increment the age by 1 year and then display the actual age 
For E.g if current age is 20 then when Birthday method is invoked ,it should print the age as 21
Isteenager method should take age as input and should check if their age is less than 14 then he is Child 
else he is Teenager.
'''

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    
    def Birthday(self, age):
        print("Happy Birthday!")
        age += 1
        print(f"Your new age is: {age}")
        self.Age = age
    
    def isteenager(self, age):
        if age < 14:
            print("Child")
        else:
            print("Teenager")


person = Person("John", 13)
print(f"Name: {person.Name}, Age: {person.Age}")
    
# Check if teenager
person.isteenager(person.Age)
    
# Celebrate birthday
person.Birthday(person.Age)
    
# Check teenager status after birthday
person.isteenager(person.Age)


'''
Problem 2:
The aim of this exercise is to create a new class called Account. 
1. Define a new class to represent a type of bank account.
2. When the class is instantiated you should provide the account number, the name of the account 
holder, an opening balance and the type of account (which can be a string representing 'current', 
'deposit' or 'investment' etc.). 
This means that there must be an __init__ method and you will need to store the data within the object. 
3. Provide three instance methods for the Account; 
deposit(amount), 
withdraw(amount) and 
get_balance(). 
The behaviour of these methods should be as expected, 
deposit will increase the balance, 
withdraw will decrease the balance and
get_balance() returns the current balance.
4. Define a simple test application to verify the behaviour of your Account class.
It can be helpful to see how your class Account is expected to be used. 
For this reason a simple test application for the Account is given below: 
The following output illustrates what the result of running this test application might look like: 
acc1 = Account('123', 'John', 10.05, 'current') 
acc2 = Account('345', 'John', 23.55, 'savings') 
acc3 = Account('567', 'Phoebe', 12.45, 'investment') 
print(acc1.display())
print(acc2.display()) 
print(acc3.display()) 
acc1.deposit(23.45) 
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())
The following output illustrates what the result of running this test application might look like:
Account[123] - John, current account = 10.05
Account[345] - John, savings account = 23.55
Account[567] - Phoebe, investment account = 12.45 
balance: 21.1
'''

class Account:
    def __init__(self, accountNumber, accountHolderName, openingBalance, accountType):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.openingBalance = openingBalance
        self.accountType = accountType
    
    def deposit(self, amount):
        print("---- DEPOSIT -------")
        print(f"Depositing {amount} into the account number {self.accountNumber}")
        self.openingBalance += amount

    def withdraw(self, amount):
        print("---- WITHDRAW ------")
        print(f"Withdrawing {amount} from the account Number {self.accountNumber}")
        self.openingBalance -= amount

    def get_balance(self):
        print('----- Current Balance -----')
        print(f"Current available balance: {self.openingBalance} for the account number : {self.accountNumber}")
        return self.openingBalance
    
    def display(self):
        return f"Account[{self.accountNumber}] - {self.accountHolderName}, {self.accountType} account = {self.openingBalance}"



acc1 = Account('123', 'John', 10.05, 'current') 
acc2 = Account('345', 'John', 23.55, 'savings') 
acc3 = Account('567', 'Phoebe', 12.45, 'investment') 


print(acc1.display())
print(acc2.display()) 
print(acc3.display()) 
acc1.deposit(23.45) 
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())
    