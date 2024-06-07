class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit_amount(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw_amount(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder


user_1 = BankAccount(9096755288, "james", 25000)
print(user_1.deposit_amount(2000))