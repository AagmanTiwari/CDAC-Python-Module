'''
Assignment 4: Relational SQLite User Management System

Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, display existing details, or register new users.

Problem Description
Create a class UserDatabaseManager that connects to a SQLite database file:

__init__(self, db_path): Connects to the database and creates a table users if it doesn't already exist:
Columns: id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, address TEXT, mobile TEXT, email TEXT.
find_user(self, username):
Queries the database for the given username using a parameterized SQL query.
If found, returns a dictionary: {"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}.
If not found, returns None.
add_or_update_user(self, username, address, mobile, email):
Checks if username exists.
If user exists, updates their address, mobile, and email values and returns "UPDATED".
If user does not exist, inserts a new record and returns "INSERTED".
list_all_users(self): Returns a list of dictionaries for all registered users ordered alphabetically by username.
Example Walkthrough
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED
'''

import sqlite3


class UserDatabaseManager:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)

        self.connection.commit()

    def add_user(self, name, email, age):

        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age)
            )

            self.connection.commit()

            print("User added successfully.")

        except sqlite3.IntegrityError:
            print("Email already exists.")

    def view_users(self):

        self.cursor.execute("SELECT * FROM users")

        users = self.cursor.fetchall()

        for user in users:
            print(user)

    def update_user(self, user_id, name, email, age):

        self.cursor.execute(
            """
            UPDATE users
            SET name = ?, email = ?, age = ?
            WHERE id = ?
            """,
            (name, email, age, user_id)
        )

        self.connection.commit()

        print("User updated successfully.")

    def delete_user(self, user_id):

        self.cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        self.connection.commit()

        print("User deleted successfully.")

    def close(self):
        self.connection.close()


database = UserDatabaseManager("users.db")

database.create_table()

database.add_user("Aagman", "aagman@example.com", 21)
database.add_user("Rahul", "rahul@example.com", 22)

print("\nUsers:")
database.view_users()

database.update_user(
    1,
    "Aagman Tiwari",
    "aagman@example.com",
    21
)

print("\nAfter update:")
database.view_users()

database.delete_user(2)

print("\nAfter delete:")
database.view_users()

database.close()
