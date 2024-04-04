""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance: float, interest: float):
        """Initializes the Account class with balance and interest"""
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance: float):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest: float):
        """Sets the interest gained for the the account"""
        self.interest = interest