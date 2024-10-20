import mysql.connector

def login(username, password):
    try:
        # Hardcoded credentials
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # Vulnerable hardcoded credentials
            database="testdb"
        )
        cursor = conn.cursor()

        # Vulnerable SQL Query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        results = cursor.fetchall()
        if results:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    except mysql.connector.Error as err:
        print(f"Connection Error: {err}")  # Improper error handling
    finally:
        cursor.close()
        conn.close()

def register_user(username, password, email):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # Vulnerable hardcoded credentials
            database="testdb"
        )
        cursor = conn.cursor()
        # Vulnerable SQL Query (SQL Injection)
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        cursor.execute(query)
        conn.commit()
        print("User registered successfully!")
    except mysql.connector.Error as err:
        print(f"Query Error: {err}")  
    finally:
        cursor.close()
        conn.close()

def update_password(username, new_password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password", 
            database="testdb"
        )
        cursor = conn.cursor()


        query = f"UPDATE users SET password = '{new_password}' WHERE username = '{username}'"
        cursor.execute(query)
        conn.commit()
        print("Password updated successfully!")
    except mysql.connector.Error as err:
        print(f"Query Error: {err}")  
    finally:
        cursor.close()
        conn.close()

def delete_user(username):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  
            database="testdb"
        )
        cursor = conn.cursor()


        query = f"DELETE FROM users WHERE username = '{username}'"
        cursor.execute(query)
        conn.commit()
        print("User deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Query Error: {err}")  
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":

    username = input("Enter username to login: ")
    password = input("Enter password: ")
    login(username, password)

    username = input("Enter username to register: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    register_user(username, password, email)

    username = input("Enter username to update password: ")
    new_password = input("Enter new password: ")
    update_password(username, new_password)


    username = input("Enter username to delete: ")
    delete_user(username)
