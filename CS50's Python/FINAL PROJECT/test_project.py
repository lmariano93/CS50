import pytest
from datetime import datetime
from project import add_income, add_expense, calculate_summary, category_summary, add_debt, view_debts, transactions, debts, categories

# Test for adding income
def test_add_income(monkeypatch):
    transactions.clear()  # Clear any previous transactions
    inputs = iter(['Salary', '1000', '01-12-2024'])  # Mock inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    add_income()  # Call the function

    assert len(transactions) == 1  # Ensure 1 transaction is added
    assert transactions[0]['type'] == 'income'
    assert transactions[0]['amount'] == 1000.0
    assert transactions[0]['description'] == 'Salary'
    assert transactions[0]['date'] == datetime(2024, 12, 1)

# Test for adding expense
def test_add_expense(monkeypatch):
    transactions.clear()  # Clear any previous transactions
    inputs = iter(['Groceries', 'Food', '200', '01-12-2024'])  # Mock inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    add_expense()  # Call the function

    assert len(transactions) == 1  # Ensure 1 transaction is added
    assert transactions[0]['type'] == 'expense'
    assert transactions[0]['amount'] == 200.0
    assert transactions[0]['category'] == 'Food'
    assert transactions[0]['date'] == datetime(2024, 12, 1)

# Test for calculating summary
def test_calculate_summary(monkeypatch):
    transactions.clear()  # Clear any previous transactions

    # Add mock transactions
    transactions.append({'type': 'income', 'amount': 1000.0, 'description': 'Salary', 'category': 'Income', 'date': datetime(2024, 12, 1)})
    transactions.append({'type': 'expense', 'amount': 200.0, 'description': 'Groceries', 'category': 'Food', 'date': datetime(2024, 12, 2)})

    # Mock inputs for start and end date
    inputs = iter(['01-12-2024', '31-12-2024'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    # Capture the printed output
    monkeypatch.setattr('builtins.print', lambda x: None)

    calculate_summary()  # Call the function

    # Here we are only testing the side effects (print) and ensuring no exceptions were raised.
    assert len(transactions) == 2  # Ensure we have 2 transactions
    assert transactions[0]['amount'] == 1000.0
    assert transactions[1]['amount'] == 200.0

# Test for category summary
def test_category_summary(monkeypatch):
    transactions.clear()  # Clear any previous transactions

    # Add mock transactions
    transactions.append({'type': 'income', 'amount': 1000.0, 'description': 'Salary', 'category': 'Income', 'date': datetime(2024, 12, 1)})
    transactions.append({'type': 'expense', 'amount': 200.0, 'description': 'Groceries', 'category': 'Food', 'date': datetime(2024, 12, 2)})

    # Mock inputs for start and end date
    inputs = iter(['01-12-2024', '31-12-2024'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    # Capture the printed output
    monkeypatch.setattr('builtins.print', lambda x: None)

    category_summary()  # Call the function

    # Check that category totals were calculated correctly
    assert transactions[0]['category'] == 'Income'
    assert transactions[1]['category'] == 'Food'

# Test for adding debt
def test_add_debt(monkeypatch):
    debts.clear()  # Clear any previous debts
    transactions.clear()  # Clear any previous transactions

    # Mock inputs for adding a debt
    inputs = iter(['Creditor1', '1000', '12', '01-01-2025'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    add_debt()  # Call the function

    # Ensure the debt is added correctly
    assert len(debts) == 1  # Ensure 1 debt is added
    assert debts[0]['creditor'] == 'Creditor1'
    assert debts[0]['total_amount'] == 1000.0
    assert round(debts[0]['monthly_payment'], 2) == 83.33  # Arredondar para 2 casas decimais
    assert debts[0]['months_remaining'] == 12


# Test for viewing debts
def test_view_debts(monkeypatch):
    debts.clear()  # Clear any previous debts

    # Add a mock debt
    debts.append({'creditor': 'Creditor1', 'total_amount': 1000.0, 'monthly_payment': 83.33, 'months_remaining': 12,
                  'first_payment_date': datetime(2025, 1, 1), 'last_payment_date': datetime(2025, 12, 31)})

    # Capture the printed output
    monkeypatch.setattr('builtins.print', lambda x: None)

    view_debts()  # Call the function

    # Ensure the debt is printed correctly
    assert len(debts) == 1  # Ensure 1 debt is present
    assert debts[0]['creditor'] == 'Creditor1'

