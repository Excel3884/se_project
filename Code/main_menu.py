from tkinter import *
from PIL import ImageTk, Image
import sales
import report

# dhmiourgia parathyrou
menu = Tk()
menu.title("FundAnalyst")
menu.iconbitmap("Images/budget_icon.ico")
menu.configure(background="#4a47a3")

# eikona me to logotypo
menu_image = ImageTk.PhotoImage(Image.open("Images/menu_image.png"))
label_image = Label(image=menu_image, background="#4a47a3")
label_image.grid(row=0, column=0, columnspan=5)

#eikones gia ta buttons
sales_image = PhotoImage(file = r"Images/sales.png")
expenses_image = PhotoImage(file = r"Images/expenses.png")
balance_image = PhotoImage(file = r"Images/images.png")
monthly_image = PhotoImage(file = r"Images/img_7322.png")
report_image = PhotoImage(file = r"Images/report.png")

#------------leitourgies koumpiwn------------#

def openSales():
    sales.SalesWindow()

def openReport():
    report.ReportWindow()

def openBudget():
    import miniaios.py

#-----------------------------------koumpia menou------------------------------#
# gia tis pwlhseis
sales_button = Button(text="Sales", padx=30, pady=0,
                      fg="#413c69", activeforeground="#413c69", bg="#009813", activebackground="#009813", image=sales_image, compound=TOP, command=openSales)
sales_button.grid(row=1, column=0, padx=10, pady=10)
sales_button.config(font=("Calibri bold", 16))

# gia ta exoda
expenses_button = Button(text="Expenses", padx=30,
                         pady=0, fg="#413c69", activeforeground="#413c69", bg="#e14900", activebackground="#e14900", image=expenses_image, compound=TOP)
expenses_button.grid(row=1, column=2, padx=10, pady=10)
expenses_button.config(font=("Calibri bold", 16))

# gia to ypoloipo
balance_button = Button(text="Balance", padx=0, pady=0,
                        fg="#413c69", activeforeground="#413c69", bg="#e1fa40", activebackground="#e1fa40", image=balance_image, compound=TOP)
balance_button.grid(row=1, column=4, padx=10, pady=10)
balance_button.config(font=("Calibri bold", 16))

# gia to mhniaio budget
monthly_button = Button(text="Monthly Budget", padx=0,
                        pady=0, fg="#413c69", activeforeground="#413c69", bg="#009bd2", activebackground="#009bd2", image=monthly_image, compound=TOP,command=openBudget)
monthly_button.grid(row=2, column=1, padx=10, pady=10)
monthly_button.config(font=("Calibri bold", 16))

# gia tis anafores
report_button = Button(text="Report", padx=30, pady=0,
                       fg="#413c69", activeforeground="#413c69", bg="#ff8a0e", activebackground="#ff8a0e", image=report_image, compound=TOP, command=openReport)
report_button.grid(row=2, column=3, padx=10, pady=10)
report_button.config(font=("Calibri bold", 16))

mainloop()
