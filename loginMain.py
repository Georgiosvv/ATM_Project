import pyodbc
from UserName import get_username
from PassWord import get_password

def get_file():
    with open("DatabaseLogin.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    connection_string = get_file()
    connection = None

    try:
        connection = pyodbc.connect(connection_string)
        #print("Connected to the database successfully!")

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Λήψη του username και του password από τον χρήστη
        username = get_username()
        password = get_password()

        # Έλεγχος αν το username και password υπάρχουν στη βάση
        query = """
                SELECT COUNT(*) 
                FROM Users
                WHERE username = ? AND pass_word = ?;
                """

        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        query2 = """SELECT roles FROM Users WHERE username = ? """
        cursor.execute(query2, username)
        result2 = cursor.fetchone()
        print(result2[0])

        if result2[0] == 'admin':
            print("You are an admin")
        else:
            print("You are a user")

        if result[0] > 0:
            print("Login successful!")
            print("Welcome",username)
        else:
            print("Invalid username or password.")



    except Exception as e:
        print("Error connecting to the database:", e)

    finally:
        # Close the connection
        print('exit')
        if connection:
            connection.close()