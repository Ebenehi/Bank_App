# StudentAccount.py

from BankAccount import BankAccount

class StudentAccount(BankAccount):
    MAX_WITHDRAWAL_PER_INSTANCE = 30000  # Lower withdrawal limit for student accounts
    CASHBACK_PERCENTAGE = 0.01  # 1% cashback on deposits
    OVERDRAFT_LIMIT = 1000  # Small overdraft limit for emergencies

    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

    def deposit_amount(self, amount):
        cashback = amount * StudentAccount.CASHBACK_PERCENTAGE
        total_amount = amount + cashback
        self._BankAccount__balance += total_amount
        return self._BankAccount__balance

    def withdraw_amount(self, amount):
        if amount > StudentAccount.MAX_WITHDRAWAL_PER_INSTANCE:
            raise ValueError("Withdrawal limit exceeded: Maximum withdrawal per instance is 30,000")
        
        if amount > (self._BankAccount__balance + StudentAccount.OVERDRAFT_LIMIT):
            raise ValueError("Insufficient balance including overdraft limit")

        self._BankAccount__balance -= amount
        return self._BankAccount__balance

    def check_eligibility_for_benefits(self):
        # Assuming eligibility is based on balance
        if self._BankAccount__balance > 500:
            return "Eligible for student benefits"
        else:
            return "Not eligible for student benefits"

    def get_balance(self):
        return self._BankAccount__balance

# Example usage
if __name__ == "__main__":
    student_account = StudentAccount(1234567890, "Alice", 1000)
    print(student_account.deposit_amount(1000))  # Deposit amount with cashback
    print(student_account.check_eligibility_for_benefits())  # Check eligibility for student benefits
    try:
        print(student_account.withdraw_amount(35000))  # Attempt to withdraw more than limit
    except ValueError as e:
        print(e)  # Expected to print "Withdrawal limit exceeded: Maximum withdrawal per instance is 30,000"
    print(student_account.withdraw_amount(20000))  # Withdraw within limit
    try:
        print(student_account.withdraw_amount(2000))  # Attempt to use overdraft
    except ValueError as e:
        print(e)  # Expected to print "Insufficient balance including overdraft limit"
