class admin:
    try:
        conn = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = conn.cursor()
        while True:
            print("Admin Menu\n1.Add user\n2.Delete user\n3.View users\n4.Exit")
            choice = int(input("Choose an option (1,2,3,4): "))

            if choice == 1:
                newUsername = input("Enter username: ")
                newPassword = input("Enter password:")
                newRole = input("Enter the role: ")
                if newRole == 'user':
                    newBalance = float(input("Enter the user's balance: "))
                    cursor.execute(
                        "INSERT INTO users (username, pass_word, roles, upoloipo) VALUES (?, ?, ?, ?)",
                        (newUsername, newPassword, newRole, newBalance)
                    )
                else:
                    cursor.execute(
                        "INSERT INTO users (username, pass_word, roles, upoloipo) VALUES (?, ?, ?, ?)",
                        (newUsername, newPassword, newRole, None)  # None for 'null' in SQL
                    )
                conn.commit()
            elif choice == 2:
                deleteUserName = input("Enter the username of the person you want to remove: ")
                cursor.execute("DELETE FROM users WHERE username = ?;",(deleteUserName))
                conn.commit()
    
            elif choice == 3:
                cursor.execute("SELECT * FROM dbo.users")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        
            elif choice == 4:
                break

    

    except Exception as e:
        print("Error connecting to the database:", e)

    finally:
        # Close the connection
        print('exit')
        if conn:
            conn.close()