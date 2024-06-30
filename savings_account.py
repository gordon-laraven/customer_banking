"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    account = Account(balance)

    # Calculate interest earned
    interest = balance * ((interest_rate/100) * (months/12))

    # Update the savings account balance by adding the interest earned
    account.balance += interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    updated_balance = balance + interest
    
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account.set_interest(interest)
    account.set_balance(0)
    account.set_balance(account.get_balance() + balance)
    
    # Return the updated balance and interest earned.
    return updated_balance, interest
