'''
Assignment 5: Transactional Banking Ledger with SQLite & ACID Rollback Management

Scenario
A financial transaction engine executes fund transfers between accounts in a SQLite database. The engine must support ACID guarantees: if any part of a transfer fails (e.g. insufficient funds, invalid account), the entire transaction must roll back cleanly.

Problem Description
Create a custom exception TransactionError(Exception). Create a class BankingLedger that manages an accounts table (account_id TEXT PRIMARY KEY, holder_name TEXT, balance REAL) and an audit_log table (tx_id INTEGER PRIMARY KEY AUTOINCREMENT, from_acc TEXT, to_acc TEXT, amount REAL, timestamp TEXT):

create_account(account_id, holder_name, initial_deposit): Adds a new account. Raises ValueError if initial_deposit < 0.
transfer_funds(from_acc, to_acc, amount):
Executes an atomic transfer of amount from from_acc to to_acc.
Deducts amount from from_acc and adds amount to to_acc.
Records an entry in the audit_log table.
Validation & Rollback Rules:
amount must be strictly positive (> 0).
Both accounts must exist in the database.
from_acc must have a sufficient balance (>= amount).
If any condition fails, raise TransactionError and execute conn.rollback().
If all checks pass, execute conn.commit().
get_balance(account_id): Returns the current balance for the given account.
Example Walkthrough
bank = BankingLedger("bank.db")
bank.create_account("ACC101", "Arham", 5000.0)
bank.create_account("ACC102", "Lisa", 2000.0)

# Valid transfer
bank.transfer_funds("ACC101", "ACC102", 1500.0)
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

# Invalid transfer (insufficient funds) -> rolled back
try:
    bank.transfer_funds("ACC101", "ACC102", 10000.0)
except TransactionError as e:
    print(e)  # Output: Insufficient funds in account ACC101

# Balances remain untouched
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0
'''
import sqlite3


class BankingLedger:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL
            )
        """)

        self.connection.commit()

    def add_account(self, account_id, name, balance):

        self.cursor.execute(
            "INSERT INTO accounts VALUES (?, ?, ?)",
            (account_id, name, balance)
        )

        self.connection.commit()

    def view_accounts(self):

        self.cursor.execute("SELECT * FROM accounts")

        accounts = self.cursor.fetchall()

        for account in accounts:
            print(account)

    def transfer_money(self, sender_id, receiver_id, amount):

        try:

            self.connection.execute("BEGIN")

            self.cursor.execute(
                "SELECT balance FROM accounts WHERE id = ?",
                (sender_id,)
            )

            sender = self.cursor.fetchone()

            if sender is None:
                raise Exception("Sender account not found.")

            if sender[0] < amount:
                raise Exception("Insufficient balance.")

            self.cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, sender_id)
            )

            self.cursor.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (amount, receiver_id)
            )

            self.connection.commit()

            print("Transfer successful.")

        except Exception as error:

            self.connection.rollback()

            print("Transfer failed:", error)
            print("Transaction rolled back.")

    def close(self):
        self.connection.close()


bank = BankingLedger("bank.db")

bank.create_table()

bank.add_account(1, "Aagman", 10000)
bank.add_account(2, "Rahul", 5000)

print("\nBefore transfer:")
bank.view_accounts()

bank.transfer_money(1, 2, 2000)

print("\nAfter transfer:")
bank.view_accounts()

bank.close()
