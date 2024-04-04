# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def request_input(prompt: str, data_type: type):
    """Request user input and validate the type of the input.
    
    Args:
        prompt (str): The message to display to the user.
        data_type (type): The data type to validate the input.
    
    Returns:
        The user input as the specified data type.
    """
    user_input = input(prompt)
    while not isinstance(user_input, data_type):
        try:
            user_input = data_type(user_input)
        except ValueError:
            print(f"Invalid input. The input must be a {data_type}.")
            user_input = input(prompt)
    return user_input

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = request_input("Enter the savings account balance: ", float)
    savings_interest = request_input("Enter the savings account interest rate: ", float)
    savings_maturity = request_input("Enter the number of months to calculate the interest earned for the savings account: ", int)    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned on the savings account is: ${interest_earned:.2f}")
    print(f"The updated savings account balance with interest earned is: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = request_input("Enter the CD account balance: ", float)
    cd_interest = request_input("Enter the CD account interest rate: ", float)
    cd_maturity = request_input("Enter the number of months to calculate the interest earned for the CD account: ", int)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned on the CD account is: ${interest_earned:.2f}")
    print(f"The updated CD account balance with interest earned is: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
