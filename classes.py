class Account:
    def __init__(self,number,pin,account_owner):
        self.number = number
        self.__pin=pin
        self.__balance=0
        self.account_owner=account_owner
        self.transaction_history=[]


    def show_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "wrong pin"

#(question1)Method to deposit and withdraw 
#method to deposit funds        
    def deposit_funds(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"you have deposited {amount}")
        else:
            print("Invalid deposit amount.")

#method to withdraw funds
    def withdraw_funds(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.transaction_history.append(f"you have withdrawn {amount}")
        else:
            print("Insufficient balance.")


#(question2)Method to display the account owner's details and current balance.
    def display_details(self):
        print(f"Account Owner is {self.account_owner} and her balance is {self.__balance}" )


#(question3) Method to update the account owner's information.
    def update_details(self, new_name, new_account_number):
        self.customer_name = new_name
        self.account_number = new_account_number
        print(f"the updated account information is {self.account_number}")



#(question4)Method to generate a statement of recent transactions.
    def account_statement(self):
        for transaction in self.transaction_history:
            print(f"{transaction}")


#(question5)Method to set an overdraft limit for the account.
    def set_overdraft(self, limit):
        self.overdraft_limit = limit
        print(f"the overdraft limit is{self.overdraft_limit}")
          

#(question6) Method to calculate and apply interest to the balance.
    def calculate_interest(self):
        monthly_interest_rate = self.interest_rate / 12
        interest_amount = self.__balance * monthly_interest_rate
        self.__balance += interest_amount
        self.transaction_history.append(f"Interest applied: ${interest_amount}")
        print({self.transaction_history})

#(question7)Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        print("Account frozen. No further transactions allowed.")

    def unfreeze_account(self):
        print("Account unfrozen. Transactions can resume.")

#(question8)Method to retrieve the history of all transactions made on the account.
    def transaction_history(self):
        return self.transaction_history


#(question9)Method to enforce a minimum balance requirement.
    def set_minimum_balance(self, minimum_balance):
        self.minimum_balance = minimum_balance
        print(f"the minimum balance is {self.minimum_balance}")


#(question10)Method to transfer funds from one account to another.
    def transfer_funds(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} to {recipient.owner}.")
        else:
            print("Insufficient balance for transfer.")


#(question11)Method to close the account and perform necessary cleanup.        
    def close_account(self):
        if self.is_open:
            self.is_open = False
            print(f"Account {self.account_number} is now closed.")
        else:
            print("Account is already closed.")