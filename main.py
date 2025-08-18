# ATM Simulator 

# Initial setup
username=input("Enter your username>>")
account_balance = 1000.0  # Starting balance
correct_pin = "7124"      # ATM PIN
daily_withdrawal_limit = 500.0
daily_withdrawn = 0.0
transaction_history = []  # List to store all transactions

def show_menu():
    """Display the main menu options"""
    print("\n" + "="*30)   #Separation double lines
    print("        ATM MAIN MENU")
    print("="*30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("="*30)

def check_balance():
    """Display current account balance"""
    print("\n" + "-"*25)
    print("    BALANCE INQUIRY")
    print("-"*25)
    print(f"Your current balance is: GHS{account_balance:.2f}")
    print("-"*25)

def deposit():
    """Handle money deposit"""
    global account_balance
    
    print("\n" + "-"*25)
    print("      DEPOSIT MONEY")
    print("-"*25)
    
    try:
        amount = float(input("Enter deposit amount: GHS"))
        
        # Check for invalid amounts
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero!")
            return
        
        # Check for unrealistic amounts (basic validation)
        if amount > 10000:
            print("Error: Maximum deposit limit is GHS10,000 per transaction!")
            return
        
        # Process deposit
        account_balance += amount
        
        # Add to transaction history
        transaction_record = f"Deposit: +GHS{amount:.2f} | Balance: GHS{account_balance:.2f}"
        transaction_history.append(transaction_record)
        
        # Print receipt
        print_receipt("Deposit", amount, account_balance)
        
    except ValueError:
        print("Error: Please enter a valid number!")

def withdraw():
    """Handle money withdrawal"""
    global account_balance, daily_withdrawn
    
    print("\n" + "-"*25)
    print("     WITHDRAW MONEY")
    print("-"*25)
    
    try:
        amount = float(input("Enter withdrawal amount: GHS"))
        
        # Check for invalid amounts
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero!")
            return
        
        # Check if enough balance
        if amount > account_balance:
            print("Error: Insufficient funds!")
            print(f"Your current balance is: GHS{account_balance:.2f}")
            return
        
        # Check daily withdrawal limit
        if daily_withdrawn + amount > daily_withdrawal_limit:
            remaining_limit = daily_withdrawal_limit - daily_withdrawn
            print(f"Error: Daily withdrawal limit exceeded!")
            print(f"Daily limit: GHS{daily_withdrawal_limit:.2f}")
            print(f"Already withdrawn today: GHS{daily_withdrawn:.2f}")
            print(f"Remaining limit: GHS{remaining_limit:.2f}")
            return
        
        # Process withdrawal
        account_balance -= amount
        daily_withdrawn += amount
        
        # Add to transaction history
        transaction_record = f"Withdrawal: -GHS{amount:.2f} | Balance: GHS{account_balance:.2f}"
        transaction_history.append(transaction_record)
        
        # Print receipt
        print_receipt("Withdrawal", amount, account_balance)
        
    except ValueError:
        print("Error: Please enter a valid number!")

def print_receipt(transaction_type, amount, current_balance):
    """Print a simple receipt for the transaction"""
    print("\n" + "-"*30)
    print("        ATM RECEIPT")
    print("-"*30)
    print(f"Transaction: {transaction_type}")
    print(f"Amount: GHS{amount:.2f}")
    print(f"New Balance: GHS{current_balance:.2f}")
    print(f"Daily Withdrawn: GHS{daily_withdrawn:.2f}")
    print("-"*30)
    print("Thank you for using our ATM!")
    print("-"*30)

def show_transaction_history():
    """Display all transaction history"""
    print("\n" + "="*40)
    print("        TRANSACTION HISTORY")
    print("="*40)
    
    if len(transaction_history) == 0:
        print("No transactions found.")
    else:
        for i, transaction in enumerate(transaction_history, 1):
            print(f"{i}. {transaction}")
    
    print("="*40)

def login():
    """Handle user login with PIN"""
    print("="*35)
    print(f"     WELCOME {username}! TO ATM STIMULATOR")
    print("="*35)
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        entered_pin = input("Please enter your PIN: ")
        
        if entered_pin == correct_pin:
            print("Login successful!")
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            
            if remaining_attempts > 0:
                print(f"Incorrect PIN! {remaining_attempts} attempts remaining.")
            else:
                print("Too many incorrect attempts. Access denied!")
                return False
    
    return False

def main():
    """Main program function"""
    # Login process
    if not login():
        print("Goodbye!")
        return
    
    # Main ATM loop
    while True:
        show_menu()
        
        try:
            choice = input("Please select an option (1-5): ")
            
            if choice == "1":
                check_balance()
            
            elif choice == "2":
                deposit()
            
            elif choice == "3":
                withdraw()
            
            elif choice == "4":
                show_transaction_history()
            
            elif choice == "5":
                print("\n" + "="*30)
                print("Thank you for using Python ATM!")
                print("Have a great day!")
                print("="*30)
                break
            
            else:
                print("Error: Invalid option! Please select 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except:
            print("An unexpected error occurred. Please try again.")

# Start the ATM program
if __name__ == "__main__":
    main()
