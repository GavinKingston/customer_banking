"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance: float=0, interest_rate: float=0, months: int=1):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
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

    # Update the CD account balance by adding the interest earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    account.set_balance(float(account.balance + interest))

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    account.set_interest(float(interest_earned))

    # Return the updated balance and interest earned.
    return float(account.balance), float(account.interest) # ADD YOUR CODE HERE
