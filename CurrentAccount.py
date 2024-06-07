from BankAccount import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

    def deposit(self, amount):
        super().deposit_amount(amount)
        return super().get_balance()

    def withdraw(self, amount):
        super().withdraw_amount(amount)
        return super().get_balance()

current_account = CurrentAccount(1994430420, "Jane Doe")
print(current_account.deposit_amount(20000))  # 20000
print(current_account.withdraw_amount(15000))  # 5000
