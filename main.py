import sqlite3
import tkinter as tk

database = "Other\DataBase.sqlite"
icon = "Other\Icon.ico"

def signIn():
    login = input_login.get()
    password = input_password.get()
    input_password.delete(0, tk.END)

    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT login, password FROM users")
    db = cursor.fetchall()
    cursor.close()

    for i in db:
        if login == i[0] and password == i[1]:
            label["text"] = "Successfully"
            break
    else:
        label["text"] = "Wrong login or password"

def registered():
    login = input_login.get()
    password = input_password.get()
    password_2 = input_password_2.get()
    input_password.delete(0, tk.END)
    input_password_2.delete(0, tk.END)


    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT login, password FROM users")
    db = cursor.fetchall()

    for i in db:
        if login == i[0]:
            label_2["text"] = "This login is already taken"
            cursor.close()
            return


    if login != "" and password != "" and password == password_2:
        cursor.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}')")
        connect.commit()
        cursor.close()
        label_2["text"] = "You have registered"
    else:
        cursor.close()
        if password != password_2:
            label_2["text"] = "Password mismatch"
            return
        label_2["text"] = "Invalid login or password"

def register():
    button_SignIn.destroy()
    button_Register.destroy()
    label.destroy()
    input_password_2.pack(pady=6, side=tk.TOP)
    button_Registered = tk.Button(text="Registered", font="Times 10 bold", command=registered)
    button_Registered.pack(pady=6)
    label_2.pack(pady=6)
    button_Registered = tk.Button(text="Return", font="Times 10 bold", command=restart)
    button_Registered.place(x=0, y=0)

def restart():
    window.destroy()
    start()


def start():
    global window, input_login, input_password, input_password_2, button_SignIn, button_Register, label, label_2
    window = tk.Tk()
    window.wm_geometry(f"300x300+800+300")
    window.title("Authencation")
    window.resizable(width=False, height=False)
    window.iconbitmap(icon)

    input_login = tk.Entry()
    input_login.pack(pady=6, side=tk.TOP)
    input_password = tk.Entry(show="*")
    input_password.pack(pady=6, side=tk.TOP)
    input_password_2 = tk.Entry(show="*")

    button_SignIn = tk.Button(window, text="Sign In", font="Times 10 bold", command=signIn)
    button_SignIn.pack(pady=6, side=tk.TOP)

    button_Register = tk.Button(text="Registered", font="Times 10 bold", command=register)
    button_Register.pack(pady=6)

    label = tk.Label(font="Times 10 bold")
    label.pack(pady=6)
    label_2 = tk.Label(font="Times 10 bold")

    window.mainloop()

if __name__ == "__main__":
    start()