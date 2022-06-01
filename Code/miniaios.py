from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import  mysql.connector
import Employee
import Operating_Cost
import Supply
import Expenses
from sales import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


total_income = 0
total_SupCost = 0
total_salaries = 0
total_opCost = 0



employees_list = []
sales_list = []
Op_Costs_list = []
supplies_list = []





conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fundanalyst"
)

cur = conn.cursor()







class Sale():

        def __init__(self, prod_id, prod_name, prod_type, prod_date, prod_price, prod_amount, prod_purchase):
            self.prod_id = prod_id
            self.prod_name = prod_name
            self.prod_type = prod_type
            self.prod_date = prod_date
            self.prod_price = prod_price
            self.prod_amount = prod_amount
            self.prod_purchase = prod_purchase

        def get_income(self):
            return self.prod_price * self.prod_amount




cur.execute("SELECT * FROM sales")
rows = cur.fetchall()



for row in rows:
    object_row = Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    sales_list.append(object_row)




for item in sales_list:
    total_income += item.get_income()

cur.execute("SELECT * FROM operatingCosts")
rows = cur.fetchall()



for row in rows:
    object_row = Operating_Cost.Operating_Cost(row[0], row[1], row[2], row[3], row[4])
    Op_Costs_list.append(object_row)




for item in Op_Costs_list:
    total_opCost += item.get_Operating_Costs()


cur.execute("SELECT * FROM Employees")

rows = cur.fetchall()


for row in rows:
   object_row = Employee.Employee(row[0], row[1], row[2], row[3], row[4])
employees_list.append(object_row)



for item in employees_list:
    total_salaries += item.getSalary()
cur.execute("SELECT * FROM Supplies")
rows = cur.fetchall()


for row in rows:
    object_row = Supply.Supply(row[0], row[1])
supplies_list.append(object_row)

total_expenses = total_SupCost +total_salaries +total_opCost

def MonthlyWindow():
    # dhmiourgia parathyrou
    monthly = Toplevel()
    monthly.title("Monthly Budget")
    monthly.iconbitmap("Images/budget_icon.ico")
    monthly.configure(background="#4a47a3")
    monthly.state("zoomed")


class App:
    def __init__(self, root):
        # setting title
        root.title("Monthly Budget")

        root.iconbitmap("Images/budget_icon.ico")
        root.configure(background="#4a47a3")

        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_780 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20)
        GLabel_780["font"] = ft
        GLabel_780["fg"] = "#23c4c6"
        GLabel_780["justify"] = "center"
        GLabel_780["text"] = "This Month"
        GLabel_780.place(x=190, y=30, width=216, height=30)

        GLabel_827 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#00a41b"
        GLabel_827["justify"] = "center"
        GLabel_827["text"] = total_income
        GLabel_827.place(x=110, y=70, width=171, height=46)
        net_profit_margin = ((total_income - total_expenses) / total_income) * 100  # ypologismos katharou kerdous
        if net_profit_margin < 10:
            messagebox.showinfo('Κίνδυνος', 'Χαμηλό Κέρδος')  # minima kindnou gia xamilo kerdos
        GLabel_926 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_926["font"] = ft
        GLabel_926["fg"] = "#ff0d0d"
        GLabel_926["justify"] = "center"
        GLabel_926["text"] = total_expenses
        GLabel_926.place(x=310, y=70, width=171, height=46)
        y = np.array([total_salaries, total_opCost, total_SupCost])
        mylabels = ["Μισθοί", "Λειτουργικά έξοδα", "Κόστος προμηθειών"]
        plt.pie(y, labels=mylabels)
        plt.show()



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


