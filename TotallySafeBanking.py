class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        # Initialize with account details and initial balance
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = initialBalance
    
    def deposit(self, amount):
        # Check if the deposit amount is positive
        if amount <= 0:
            print("You can't deposit zero or negative amounts. Try again with real money.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")
    
    def withdraw(self, amount):
        # Check if the withdrawal amount is positive
        if amount <= 0:
            print("Are you just pushing my buttons, or did you mean to make a deposit?")
            return
        # Check if the withdrawal amount is more than the balance
        if amount > self.__balance:
            print(f"So you'd like {amount}? You've only got {self.__balance}. You do the math.")
            return
        self.__balance -= amount
        print(f"You took out {amount}. Now you have {self.__balance} left.")
    
    def getBalance(self):
        # Return the current balance
        return self.__balance
    
    def displayAccountInfo(self):
        # Display the account information
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Balance: {self.__balance}")

if __name__ == "__main__":
    
# Testing area, put a # in front of the ''' in the line below, and the one at EOF.
    '''
    # # Create some bank accounts
    account1 = BankAccount("000001", "Johnny Mnemonic", 1000.0)
    account2 = BankAccount("000002", "Henry Rollins", 2000.0)
    
    # # Display account information
    print("Account 1 Info:")
    account1.displayAccountInfo()
    
    print("\nAccount 2 Info:")
    account2.displayAccountInfo()
    
    # # Perform some transactions
    print("\nDoin' stuff with the first test account:")
    account1.deposit(5000)
    account1.withdraw(250)
    account1.withdraw(20000)  # This should display an error
    
    print("\nDoin' stuff with the second test account:")
    account2.deposit(1000)
    account2.withdraw(999)
    
    # # Display account information again to see changes
    print("\nUpdated Account Info:")
    account1.displayAccountInfo()
    
    # print("\nUpdated Account Info:")
    account2.displayAccountInfo()

    comment out this line with a # to test '''