from tkinter import *
from tkinter import messagebox
import mysql.connector
import auth
def login():
    username = username_a.get()
    password = password_b.get()
    # Check the credentials against the MySQL database
    if username == "suraj" and password == "suraj":
        messagebox.showinfo("Login", "Login successful!")
        auth.open_dashboard()

    else:
        messagebox.showerror("Login Failed", "Each Field Required")
def register():
    username =username_a.get()
    password =password_b.get()

    # Register the user in the MySQL database
    if register_user(username, password):
        messagebox.showinfo("Register", "Registration successful!")
    else:
        messagebox.showerror("Register", "Registration failed.")
def cancel():
    window.destroy()


def check_credentials(username, password):
    # Establish the connection to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pro_alg_2_1"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SQL query to check the username and password
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Return True if the credentials are correct, False otherwise
    return result is not None


def register_user(username, password):
    # Establish the connection to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pro_alg_2_1"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SQL query to insert the new user into the database
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)

    try:
        cursor.execute(query, values)
        db.commit()
        # Close the cursor and database connection
        cursor.close()
        db.close()
        return True
    except:
        db.rollback()
        # Close the cursor and database connection
        cursor.close()
        db.close()
        return False


# Create the main window
window =Tk()
window.title("Login Page")
window.config(bg='skyblue')

# Set the window size and position
window.geometry("700x400")
window.resizable(False, False)


Label(text="Enter Login Information",font="comiscsansms 15 bold ",bg='skyblue', justify='center').grid(row=0,columnspan=2)
# Create labels and entry fields for username and password
Label(text="Username: ",font="comiscsansms 10 bold italic",bg='skyblue',pady=20,justify='center').grid(row=1,column=0)
Label(text="Password: ",font="comiscsansms 10 bold italic",bg='skyblue').grid(row=2,column=0)
username_a=StringVar()
password_b=StringVar()
Entry(textvariable=username_a).grid(row=1,column=1)
Entry(textvariable=password_b).grid(row=2,column=1)


# Create the login, register, and cancel buttons
Button(text="Submit",padx=10,command=login).grid(row=7,column=0)
Button(text="Register",padx=10,command=register).grid(row=7,column=1)
Button(text="Cancel",padx=10,command=cancel).grid(row=7,column=2)
# Run the main window's event loop
window.mainloop()
