from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import font

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
root.geometry("800x850")
small_font = font.Font(size=18)
lb=Listbox(root,height=5,width=40,font=small_font)
lb.grid(row=8,column=1,columnspan=6)
list_label = Label(root, text="Existing Accounts:", fg="#709fb0", bg="#4a47a3")
list_label.grid(row=6, column=1, padx=150, pady=10, sticky="w")
list_label.config(font=("Calibri", 22))
explain_label = Label(root, text="username  password  name   surname  IsOwner", fg="#709fb0", bg="#4a47a3")
explain_label.grid(row=7, column=1, padx=10, pady=10, sticky="w")
explain_label.config(font=("Calibri", 20))
delete_label = Label(root, text="                type below username to delete", fg="#709fb0", bg="#4a47a3")
delete_label.grid(row=9, column=1, padx=10, pady=10, sticky="w")
delete_label.config(font=("Calibri", 20))

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

# gia to name
name_label = Label(root, text="name", fg="#709fb0", bg="#4a47a3")
name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
name_label.config(font=("Calibri", 20))
name = Entry(root, width=35, show="")
name.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
name.config(font=("Calibri", 20))

# gia to surname
surname_label = Label(root, text="surname", fg="#709fb0", bg="#4a47a3")
surname_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
surname_label.config(font=("Calibri", 20))
surname = Entry(root, width=35, show="")
surname.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
surname.config(font=("Calibri", 20))

# gia to owner
owner_label = Label(root, text="owner", fg="#709fb0", bg="#4a47a3")
owner_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
owner_label.config(font=("Calibri", 20))
owner = Entry(root, width=35, show="")
owner.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
owner.config(font=("Calibri", 20))

#gia to delete
delete = Entry(root, width=35, show="")
delete.grid(row=9, column=1, columnspan=2, padx=10, pady=10)
delete.config(font=("Calibri", 20))

def viewall():
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    rows = cur.fetchall()
    conn.close()
    lb.delete(0, END)
    return rows




for row in viewall():
    lb.insert(END, row)



def onClick():
    username_input = username.get()
    password_input = password.get()
    name_input = name.get()
    surname_input = surname.get()
    owner_input = owner.get()
    cur.execute("INSERT INTO account VALUES(%s,%s,%s,%s,%s)",(username_input,password_input,name_input,surname_input,owner_input))
    row = cur.fetchone()

def onClickDel():
    delete_input = delete.get()

    cur.execute("DELETE FROM account WHERE username=?", delete_input)
    conn.commit()
    row = cur.fetchone()


create_button = Button(root, text="Create", padx=40,
                      fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=onClick)
create_button.grid(row=5, column=1, pady=10, padx=10)
create_button.config(font=("Calibri", 24))

delete_button = Button(root, text="delete", padx=40,
                      fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=onClickDel)
delete_button.grid(row=10, column=1, pady=10, padx=10)
delete_button.config(font=("Calibri", 24))


mainloop()
