import tkinter
import Expenses
import sales
import dbConnection
from tkinter import *

# sundesh sth vash dedomenwn

conn = dbConnection.conn

cur = conn.cursor()


def BudgetWindow():
    # dhmiourgia parathyrou
    budget = Toplevel()
    budget.title("Expenses")
    budget.iconbitmap("Images/Sales_icon.ico")
    budget.configure(background="#4a47a3")
    budget.state("zoomed")

    #---------lista eggrafwn-----------#

    class Budget(Expenses, sales):

        def __init__(self, month):
            self.month=month

        """
        def totalSales():
            return sales.get_income() #auti epistrefei synoliko, den yparxei adistoixi methodos gia sygekrimeno mina
            
        def totalExpenses():
            Expenses.create_table_Op_Costs('', '')
            return Expenses.total_expenses_range()

        def totalBudget():
            return sales.get_income() - Expenses.total_expenses()
        """
