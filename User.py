from database import create_connection, login, get_balance, update_balance 

def user_menu(conn, user_id):
    while True:
        print("\n1. Ανάληψη")
        print("2. Κατάθεση")
        print("3. Ερώτηση υπολοίπου")
        print("4. Έξοδος")
        choice = input("Επιλέξτε ενέργεια: ")
        if choice == '1':
            amount = float(input("Εισαγάγετε ποσό: "))
            update_balance(conn, user_id, -amount)
        elif choice == '2':
            amount = float(input("Εισαγάγετε ποσό: "))
            update_balance(conn, user_id, amount)
        elif choice == '3':
            balance = get_balance(conn, user_id)
            print(f"Το υπόλοιπό σας: {balance}")
        elif choice == '4':
            break
        else:
            print("Λανθασμένη εισαγωγή")

def main():
    conn = create_connection()
    if conn is not None:
        print("Καλώς ήρθατε στο User!")
        username = input("Πληκτρολογήστε username: ")
        password = input("Πληκτρολογήστε password: ")
        user_id = login(conn, username, password)
        if user_id:
            user_menu(conn, user_id)
        else:
            print("Μη έγκυρο όνομα χρήστη ή κωδικός πρόσβασης")
        conn.close()
    else:
        print("Σφάλμα σύνδεσης βάσης δεδομένων!")

if __name__ == '__main__':
    main()
