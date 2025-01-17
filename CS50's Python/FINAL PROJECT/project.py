import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from tabulate import tabulate

# Sample transaction data and debts
transactions = []
debts = []
categories = ["Food", "Transport", "Entertainment", "Utilities", "Health", "Other", "Debt"]  # 'Debt' added to categories

# Main function to drive the program
def main():
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Analyze by Category (Summary)")
        print("5. Analyze by Category (Detail)")
        print("6. Add Debt")
        print("7. Track Debts")
        print("8. Report")
        print("9. Exit")

        choice = input("Select a Number: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            category_detail()
        elif choice == "6":
            add_debt()
        elif choice == "7":
            view_debts()
        elif choice == "8":
            report()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Generic function to add income or expense
def add_transaction(transaction_type):
    description = input("Enter a description: ")
    category = "Income" if transaction_type == "income" else input(f"Enter a category from the following options: {', '.join(categories)}: ").capitalize()

    if transaction_type == "expense":
        while category not in categories:
            category = input(f"Invalid category. Please select a valid category from the following options: {', '.join(categories)}: ").capitalize()

    amount = validate_amount()
    if amount is None:
        return

    date = validate_date()
    if date is None:
        return

    transaction = {
        'type': transaction_type,
        'description': description,
        'category': category,
        'amount': amount,
        'date': date
    }
    transactions.append(transaction)
    print(f"{transaction_type.capitalize()} added successfully!")

# Function to add income
def add_income():
    return add_transaction('income')

# Function to add expense
def add_expense():
    return add_transaction('expense')

# Helper function to validate amount input
def validate_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return None
        return amount
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return None

# Helper function to validate date input
def validate_date():
    try:
        date_input = input("Enter the date (DD-MM-YYYY): ")
        date = datetime.strptime(date_input, "%d-%m-%Y")
        return date
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return None

# Function to calculate and display a summary of income, expenses, and balance
def calculate_summary():
    print("\nEnter the date range for the summary:")

    # Validate the start date
    start_date = validate_date()
    if start_date is None:
        return

    # Validate the end date
    end_date = validate_date()
    if end_date is None:
        return

    # Filter transactions by date range
    filtered_transactions = [t for t in transactions if start_date <= t['date'] <= end_date]

    # Calculate totals based on the filtered transactions
    total_income = sum(t['amount'] for t in filtered_transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in filtered_transactions if t['type'] == 'expense')
    total_debt = sum(t['amount'] for t in filtered_transactions if t['category'] == 'Debt')  # Include debts
    balance = total_income - total_expense - total_debt

    # Display the summary
    print("\nSummary:")
    print(f"Date Range: {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Total Debts: {total_debt}")
    print(f"Balance: {balance}")

# Function to display a summary of transactions by category
def category_summary():
    print("\nCategories summary:")
    # Initialize dictionary with all categories, including 'Income' and 'Debt'
    category_totals = {category: 0 for category in categories}
    category_totals['Income'] = 0

    start_date = validate_date()
    if start_date is None:
        return

    end_date = validate_date()
    if end_date is None:
        return

    for t in transactions:
        if start_date <= t['date'] <= end_date:
            # Sum amount for valid categories ('Income' or 'Expense')
            if t['category'] in category_totals:
                category_totals[t['category']] += t['amount']

    # Display the summary table
    table = [[category, f"{total:.2f}"] for category, total in category_totals.items()]
    print(tabulate(table, headers=["Category", "Total"], tablefmt="pretty"))

# Function to display detailed transactions for a selected category
def category_detail():
    print("\nCategories:")
    # Include 'Income', 'Expense', and 'Debt' categories as well
    all_categories = categories + ['Income', 'Expense', 'Debt']
    for idx, category in enumerate(all_categories, start=1):
        print(f"{idx}. {category}")

    try:
        category_choice = int(input(f"Select a category (1-{len(all_categories)}): "))
        if category_choice < 1 or category_choice > len(all_categories):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please select a valid category.")
        return

    category = all_categories[category_choice - 1]

    start_date = validate_date()
    if start_date is None:
        return

    end_date = validate_date()
    if end_date is None:
        return

    # Filter transactions by category, including 'Income', 'Expense', and 'Debt'
    filtered_transactions = [t for t in transactions if t['category'] == category and start_date <= t['date'] <= end_date]
    # Sort by date, oldest first
    filtered_transactions.sort(key=lambda x: x['date'])
    if filtered_transactions:
        table = [[t['description'], t['amount'], t['date'].strftime("%d-%m-%Y")] for t in filtered_transactions]
        print(tabulate(table, headers=["Description", "Amount", "Date"], tablefmt="pretty"))
    else:
        print(f"No transactions found in category '{category}' for the selected date range.")

# Function to add a debt
def add_debt():
    creditor = input("Enter the creditor's name: ")

    total_amount = validate_amount()
    if total_amount is None:
        return

    try:
        months_remaining = int(input("How many months will it take to pay off this debt? "))
        if months_remaining <= 0:
            print("Months remaining must be positive.")
            return
    except ValueError:
        print("Invalid input for months. Please enter a positive integer.")
        return

    # Clarify the request for the first payment date
    print("First Payment - ", end="")
    first_payment_date = validate_date()
    if first_payment_date is None:
        return

    # Create the debt as a series of expenses
    monthly_payment = total_amount / months_remaining
    for month in range(months_remaining):
        # Calculate the next payment date using relativedelta to handle the month rollover
        next_payment_date = first_payment_date + relativedelta(months=+month)

        # Adjust the date to the last day of the month if necessary
        last_day_of_month = calendar.monthrange(next_payment_date.year, next_payment_date.month)[1]
        if next_payment_date.day > last_day_of_month:
            next_payment_date = next_payment_date.replace(day=last_day_of_month)

        # Add each payment as an "expense"
        transactions.append({
            'type': 'expense',
            'description': f"Debt payment to {creditor}",
            'category': 'Debt',
            'amount': monthly_payment,
            'date': next_payment_date
        })

    # Calculate the last payment date (last month)
    last_payment_date = first_payment_date + relativedelta(months=+months_remaining-1)
    last_day_of_last_month = calendar.monthrange(last_payment_date.year, last_payment_date.month)[1]
    if last_payment_date.day > last_day_of_last_month:
        last_payment_date = last_payment_date.replace(day=last_day_of_last_month)

    # Add the debt to the debts list with 'last_payment' included
    debts.append({
        'creditor': creditor,
        'total_amount': total_amount,
        'monthly_payment': monthly_payment,
        'months_remaining': months_remaining,
        'first_payment_date': first_payment_date,
        'last_payment_date': last_payment_date  # This is the key that will solve your issue
    })

    print(f"Debt added successfully for {creditor}. Total amount: {total_amount}, Monthly payment: {monthly_payment:.2f}.")

def view_debts():
    if debts:
        for debt in debts:
            print(f"Creditor: {debt['creditor']} - Total Amount: {debt['total_amount']} - Monthly Payment: {debt['monthly_payment']} - Months Remaining: {debt['months_remaining']} - First Payment: {debt['first_payment_date'].strftime('%d-%m-%Y')} - Last Payment: {debt['last_payment_date'].strftime('%d-%m-%Y')}")
    else:
        print("No debts found.")


# Function to report transactions within a date range
def report():
    start_date = validate_date()
    if start_date is None:
        return

    end_date = validate_date()
    if end_date is None:
        return

    filtered_transactions = [t for t in transactions if start_date <= t['date'] <= end_date]
    # Sort by date, oldest first
    filtered_transactions.sort(key=lambda x: x['date'])
    if filtered_transactions:
        table = [[t['description'], t['amount'], t['category'], t['date'].strftime("%d-%m-%Y")] for t in filtered_transactions]
        print(tabulate(table, headers=["Description", "Amount", "Category", "Date"], tablefmt="pretty"))
    else:
        print("No transactions found in the given date range.")

if __name__ == "__main__":
    main()
