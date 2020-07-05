import random

class Customer:
    
    def __init__(self,full_name,full_address):
        self.full_name = full_name
        self.full_address = full_address
    
    def openBankAccount(self):
        self.account_number = random.randrange(1, 10**3)
        self.balance = 0.00
        print(f'Bank account opened with account number {self.account_number}')
    
    def closeBankAccount(self):
        self.balance = 0.00
    
    def checkBalance(self):
        print(f'Your balance is {self.balance}')
    
    def deposite(self,amount):
        self.balance += amount
        print(f'Deposite of amount {amount} is successfully completed')
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'withdraw complete of amount {amount}') 
        else:
            print('Insufficient balance')
            
if __name__ == "__main__":
    customer = Customer('Binita Thapa',"Kathmandu")
    customer.openBankAccount()
    customer.deposite(500)
    customer.withdraw(100)
    customer.checkBalance()