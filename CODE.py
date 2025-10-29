import sys
from io import StringIO

# Simulate console inputs (replace with your actual inputs)
sys.stdin = StringIO("user1\n1234\n1\n5\ny\n")  # Example: username, PIN, menu choice, etc.

# ATM Management System
# Project for Class 12 CBSE Computer Science
# Features: Login, View Balance, Withdraw, Deposit, Change PIN, Error Handling

import sys  # For exiting the program

# Dictionary to store user data (in a real system, this could be a database or file)
users = {
    "Simran": {"pin":"2007", "balance":1000000},
    "user1": {"pin": "1234", "balance": 1000},
    "user2": {"pin": "5678", "balance": 500},
    "admin": {"pin": "0000", "balance": 0}  # Example admin with no balance
}

def login():
    """Handles user login with username and PIN."""
    username = input("Enter username: ").strip()
    if username not in users:
        print("Invalid username. Try again.")
        return None
    pin = input("Enter PIN: ").strip()
    if users[username]["pin"] != pin:
        print("Invalid PIN. Try again.")
        return None
    print(f"Login successful! Welcome, {username}.")
    return username

def view_balance(username):
    """Displays the account balance."""
    balance = users[username]["balance"]
    print(f"Your current balance is: ₹{balance}")

def withdraw_cash(username):
    """Handles cash withdrawal in multiples of 10."""
    try:
        amount = int(input("Enter amount to withdraw (must be multiple of 10): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount % 10 != 0:
            print("Amount must be a multiple of 10.")
            return
        if amount > users[username]["balance"]:
            print("Insufficient balance.")
            return
        users[username]["balance"] -= amount
        print(f"Withdrawal successful! ₹{amount} withdrawn. New balance: ₹{users[username]["balance"]}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def deposit_cash(username):
    """Handles cash deposit in multiples of 10."""
    try:
        amount = int(input("Enter amount to deposit (must be multiple of 10): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount % 10 != 0:
            print("Amount must be a multiple of 10.")
            return
        users[username]["balance"] += amount
        print(f"Deposit successful! ₹{amount} deposited. New balance: ₹{users[username]["balance"]}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def change_pin(username):
    """Allows the user to change their PIN."""
    current_pin = input("Enter current PIN: ").strip()
    if users[username]["pin"] != current_pin:
        print("Incorrect current PIN.")
        return
    new_pin = input("Enter new PIN (4 digits): ").strip()
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return
    confirm_pin = input("Confirm new PIN: ").strip()
    if new_pin != confirm_pin:
        print("PINs do not match.")
        return
    users[username]["pin"] = new_pin
    print("PIN changed successfully!")

def main_menu(username):
    """Displays the main menu after login."""
    while True:
        print("\n--- ATM Menu ---")
        print("1. View Account Statement (Balance)")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Logout")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_balance(username)
        elif choice == "2":
            withdraw_cash(username)
        elif choice == "3":
            deposit_cash(username)
        elif choice == "4":
            change_pin(username)
        elif choice == "5":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

def main():
    """Main function to run the ATM system."""
    print("Welcome to the ATM Management System!")
    while True:
        username = login()
        if username:
            main_menu(username)
        choice = input("Do you want to exit? (y/n): ").strip().lower()
        if choice == "y":
            print("Thank you for using the ATM. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
