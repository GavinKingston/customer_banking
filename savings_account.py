"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance: float=0.00, interest_rate: float=0.00, months: int=1):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

    # Validate input values
    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    if months <= 0:
        raise ValueError("Months must be a positive integer.")
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    account = Account(balance, 0)

    # Calculate interest earned
    interest = account.balance * ((interest_rate / 100) * (months / 12))
    interest_earned = float(account.interest + interest)

    # Update the savings account balance by adding the interest earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account.set_balance(float(account.balance + interest))

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account.set_interest(float(interest_earned))

    # Return the updated balance and interest earned.
    return float(account.balance), float(account.interest)
