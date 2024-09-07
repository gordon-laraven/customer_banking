# Banking Application README

## Overview
This Python banking application allows users to create savings and certificate of deposit (CD) accounts. The application calculates the interest earned on the balance for a specified period, updates the account balance, and displays the results to the user.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Functions](#functions)
- [Challenge Instructions](#challenge-instructions)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create savings and CD accounts.
- Calculate interest earned based on user input.
- Update account balances after interest calculation.
- User-friendly terminal interface for input.

## Technologies Used
- Python 3.x

## Installation
To start using this application, ensure you have Python 3.x installed on your machine. Clone or download this repository to your local machine.

```bash
git clone https://github.com/yourusername/banking_application.git
cd banking_application
```

## Usage
To run the application, use the following command in your terminal:

```bash
python customer_banking.py
```

Follow the prompts to enter your account balance, interest rate, and duration in months.

## Code Structure
The application is separated into multiple files for better organization:
- `Account.py`: Defines the `Account` class with balance and interest attributes.
- `savings_account.py`: Contains the function `create_savings_account` to manage savings accounts.
- `cd_account.py`: Contains the function `create_cd_account` to manage CD accounts.
- `customer_banking.py`: Main entry point for user interaction.

## Functions

### Account Class
```python
class Account:
    def __init__(self, balance, interest):
        ...
    def set_balance(self, balance):
        ...
    def set_interest(self, interest):
        ...
```

### create_savings_account
```python
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): Initial savings account balance.
        interest_rate (float): APR interest rate.
        months (int): Length of duration.
    Returns:
        tuple: Updated balance and interest earned.
    """
```

### create_cd_account
```python
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): Initial CD account balance.
        interest_rate (float): APR interest rate.
        months (int): Length of duration.
    Returns:
        tuple: Updated balance and interest earned.
    """
```

### main
```python
def main():
    """Main function to handle user input and display account information."""
```

## Challenge Instructions
The starter files for this project consist of the following files: **Accounts.py**, **savings_account.py**, **cd_account.py**, and **customer_banking.py**.

1. **Accounts.py**:
   - Contains the `Account` class with methods to set the balance and interest for any banking account.

2. **savings_account.py**:
   - Import the `Account` class.
   - Implement the `create_savings_account` function which:
     - Creates an instance of the `Account` class with the initial balance and a default interest of `0`.
     - Calculates the interest earned based on user inputs of balance, interest rate, and duration in months.
     - Updates the account's balance by adding the calculated interest.
     - Returns the updated balance and the interest earned.

3. **cd_account.py**:
   - Import the `Account` class.
   - Implement the `create_cd_account` function which:
     - Creates a CD account instance using the `Account` class.
     - Calculates the interest earned similarly based on user inputs.
     - Updates the balance accordingly and returns the updated balance and interest earned.

4. **customer_banking.py**:
   - Import both `create_savings_account` and `create_cd_account` functions.
   - Define the main function that:
     - Prompts the user for inputs regarding their savings and CD accounts.
     - Calls the appropriate functions to perform calculations.
     - Displays the interest earned and updates the balances.

### Implementation Steps
- Create the Savings Account Function:
    - Import the `Account` class from the `Accounts.py` file.
    - Define a function that creates an instance of the `Account` class.
    - Add functionality to calculate and update the account balance with interest earned.

- Create the CD Account Function:
    - Similar to the Savings Account function but applied for CD accounts.
    - Ensure that the updated balance and interest are correctly calculated and set.

- Main Function:
    - Import necessary functions.
    - Prompt the user for input values including balances and interest rates.
    - Call the respective account creation functions.
    - Print the results in a user-friendly format.

## Example Usage
1. Launch the application.
2. Input the savings account balance, interest rate, and duration in months when prompted.
3. Review the earnings and updated account balance.
4. Repeat the process for the CD account.

```plaintext
Set your savings account balance: 1000
Set your savings account interest rate: 5
Select the number of months for your savings account: 12
Interest earned: 50.0
Updated savings account balance with interest earned: 1050.0

Enter your CD account balance: 2000
Enter your CD account interest rate: 4
Enter the number of months for your CD account: 6
Interest earned: 40.0
Updated CD account balance with interest earned: 2040.0
```

---

This README serves as the comprehensive guide to using the banking application, explaining its functionality, structure, and usage in a clear and structured format.