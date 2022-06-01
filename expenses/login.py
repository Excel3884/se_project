from tkinter import *
import mysql.connector
from tkinter import messagebox

# sundesh sth vash dedomenwn
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fundanalyst"
)

cur = conn.cursor()

# dhmiourgia parathyrou
root = Tk()
root.title("Login")
root.iconbitmap("Images/budget_icon.ico")
root.configure(background="#4a47a3")

# gia to username
username_label = Label(root, text="Username", fg="#709fb0", bg="#4a47a3")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
username_label.config(font=("Calibri", 20))
username = Entry(root, width=35)
username.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
username.config(font=("Calibri", 20))

# gia to password
password_label = Label(root, text="Password", fg="#709fb0", bg="#4a47a3")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
password_label.config(font=("Calibri", 20))
password = Entry(root, width=35, show="*")
password.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
password.config(font=("Calibri", 20))

# elegxos stoixeiwn
def onClick():
    username_input = username.get()
    password_input = password.get()
    cur.execute("SELECT * FROM accounts WHERE username=%s AND password=%s",
                (str(username_input), str(password_input)))
    row = cur.fetchone()
    if (row == None):
        messagebox.showwarning("Error", "Wrong username or password!")
    else:
        messagebox.showinfo("Success!", "You are logged in!")
        root.destroy()
        import main_menu # anoigma menou


login_button = Button(root, text="Submit", padx=40,
                      fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=onClick)
login_button.grid(row=2, column=1, pady=10, padx=10)
login_button.config(font=("Calibri", 24))

mainloop()
