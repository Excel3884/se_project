from tkinter import *
import  mysql.connector
import table

import Employee
import Operating_Cost
import Supply


# sundesh sth vash dedomenwn

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fundanalyst"
)

cur = conn.cursor()



def ExpensesWindow():
    # dhmiourgia parathyrou
    expenses_costs = Toplevel()
    expenses_costs.title("Expenses")
    expenses_costs.iconbitmap("Images/budget_icon.ico")
    expenses_costs.configure(background="#4a47a3")
    expenses_costs.state("zoomed")

    def show_opcost():
        # dhmiourgia parathyrou
        global oper_costs
        oper_costs = Toplevel()
        oper_costs.title("Operating_Costs")
        oper_costs.configure(background="#4a47a3")
        oper_costs.state("zoomed")
        create_table_Op_Costs('', '')

    def show_salaries():
        # dhmiourgia parathyrou
        global sal_costs
        sal_costs = Toplevel()
        sal_costs.title("Employees")
        sal_costs.configure(background="#4a47a3")
        sal_costs.state("zoomed")
        create_table_Salaries('')

    def show_supplies():
        # dhmiourgia parathyrou
        global sup_costs
        sup_costs = Toplevel()
        sup_costs.title("Supplies")
        sup_costs.configure(background="#4a47a3")
        sup_costs.state("zoomed")
        create_table_Supplies('', '')


    # -----------------------------------koumpia eksodwn------------------------------#
    # gia ta operating costs
    opcost_button = Button(expenses_costs, text="Operating_Costs", padx=30, pady=20,
                          fg="#413c69", activeforeground="#413c69", bg="#e1fa40", activebackground="#009813",
                           command=show_opcost)
    opcost_button.grid(row=1, column=0, padx=10, pady=10)
    opcost_button.config(font=("Calibri bold", 16))

    # gia tous ypalilous
    employee_button = Button(expenses_costs, text="Employees", padx=30,
                             pady=20, fg="#413c69", activeforeground="#413c69", bg="#e1fa40", activebackground="#e14900",
                               command=show_salaries)
    employee_button.grid(row=1, column=2, padx=10, pady=10)
    employee_button.config(font=("Calibri bold", 16))

    # gia tis promithies
    supply_button = Button(expenses_costs ,text="Supplies", padx=30, pady=20,
                            fg="#413c69", activeforeground="#413c69", bg="#e1fa40", activebackground="#e1fa40",
                               command=show_supplies)
    supply_button.grid(row=1, column=4, padx=10, pady=10)
    supply_button.config(font=("Calibri bold", 16))



    #---------lista eggrafwn-----------#


    class Expenses():

        def __init__(self):
            self.outcome = 0




    Op_Costs_list = [] # lista me ta eksoda leitoyrgias ws objects
    
    cur.execute("SELECT * FROM operatingcosts")
    rows = cur.fetchall()
    for row in rows:
        object_row = Operating_Cost.Operating_Cost(row[0], row[1], row[2], row[3], row[4])
        Op_Costs_list.append(object_row)

    
    #------------dhmiourgia pinaka--------------#

    def create_table_Op_Costs( first_date, last_date):

        values = []
        values.append(["Reyma", "Nero", "Tilefono", "Rent", "Date"])
        if len(first_date) == 0 or len(last_date) == 0: # an toulaxiston ena entry einai adeio prosthese oles tis eggrafes
            for item in Op_Costs_list:
                values.append([item.reyma, item.nero, item.tilefono, item.rent, item.date])
        else: # alliws mono osa ikanopoioun ta filtra
            for item in Op_Costs_list:
                if (str(item.date) >= first_date and str(item.date) <= last_date):
                    values.append([item.reyma, item.nero, item.tilefono, item.rent, item.date])


        global total_rows
        global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn eksodwn
        total_opCost = 0
        for item in Op_Costs_list:
            total_opCost += item.get_Operating_Costs()

        #ypologismwn synolikwn eksodwn gia epilegmeno diastima
        total_opCost_range = 0
        for item in values[1:]:
            if item:
                for j in range(total_columns-1):
                    total_opCost_range += float(item[j])
            else:
                total_opCost_range = total_opCost

            
        total_opCost=total_opCost_range
        global records_list1
        records_list1 =table.Table(oper_costs, total_rows, total_columns, values, total_opCost)

        # button gia ta filtra sta operating costs
        global filters_button1
        filters_button1 = Button(oper_costs, text="Filters", padx=100, fg="#4180fb", bg="#413c69",
                                activebackground="#413c69", activeforeground="#4180fb", command=open_filters)
        filters_button1.config(font=("Calibri", 24))
        filters_button1.grid(row=total_rows + 2, column=0, padx=20, pady=20, columnspan=3)






    #------------dhmiourgia pinaka--------------#

    def create_table_Salaries(date_in):
        employees_list = []  # lista me ta eksoda misthwn ypallilwn

        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            object_row = Employee.Employee(row[0], row[1], row[2], row[3], row[4])
            employees_list.append(object_row)

        values = []
        values.append(["Name", "Lastname", "ID", "Salary", "Month"])
        if len(date_in) == 0 : # an den dinetai minas prosthese oles tis eggrafes
            for item in employees_list:
                values.append([item.name, item.lastname, item.id, item.salary, item.month])
        else: # alliws mono tous misthous tou mina pou dothike
            for item in employees_list:
                d=str(item.month)
                if (d[5:6] == date_in[5:6]):
                    values.append([item.name, item.lastname, item.id, item.salary, item.month])


        global total_rows
        global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn eksodwn misthwn
        total_salaries = 0
        for item in employees_list:
            total_salaries += item.getSalary()

        #ypologismwn synolikwn eksodwn misthwn gia epilegmeno diastima
        total_salaries_month = 0
        for item in values[1:]:
            if item:
                total_salaries_month  +=float( item[3])
            else:
                total_salaries_month  = total_salaries


        total_salaries = total_salaries_month
        global records_list2
        records_list2=table.Table(sal_costs, total_rows, total_columns, values, total_salaries)

        # button gia ta filtra stous employies
        global filters_button2
        filters_button2 = Button(sal_costs, text="Filters", padx=100, fg="#4180fb", bg="#413c69",
                                activebackground="#413c69", activeforeground="#4180fb", command=open_filters)
        filters_button2.config(font=("Calibri", 24))
        filters_button2.grid(row=total_rows + 2, column=0, padx=20, pady=20, columnspan=3)


        global filters_button4
        filters_button4 = Button(sal_costs, text="Change Salary", padx=100, fg="#4180fb", bg="#413c69",
                                 activebackground="#413c69", activeforeground="#4180fb", command=open_salary)
        filters_button4.config(font=("Calibri", 24))
        filters_button4.grid(row=total_rows + 2, column=3, padx=20, pady=20, columnspan=3)

    def change_salary(id_emp, new_salary):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fundanalyst"
        )

        cur = conn.cursor()

        employees_list = []  # lista me ta eksoda misthwn ypallilwn

        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            object_row = Employee.Employee(row[0], row[1], row[2], row[3], row[4])
            employees_list.append(object_row)

        for item in employees_list:
            if (item.getID()==int(id_emp)):
                item.setSalary(new_salary)
                cur.execute("UPDATE employees SET salary=%s WHERE id=%s", str(new_salary), str(id_emp))
        for item in records_list2.cells_list:
            item.destroy()
        filters_button2.destroy()
        filters_button4.destroy()

        employees_list = []  # lista me ta eksoda misthwn ypallilwn

        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            object_row = Employee.Employee(row[0], row[1], row[2], row[3], row[4])
            employees_list.append(object_row)


        create_table_Salaries('')


          





    supplies_list = [] # lista me ta eksoda promitheiwn

    cur.execute("SELECT * FROM supplies")
    rows = cur.fetchall()
    for row in rows:
        object_row = Supply.Supply(row[0], row[1])
        supplies_list.append(object_row)

    #------------dhmiourgia pinaka--------------#

    def create_table_Supplies(first_date, last_date):

        values = []
        values.append(["Cost", "Date"])
        if len(first_date) == 0 or len(last_date) == 0: # an toulaxiston ena entry einai adeio prosthese oles tis eggrafes
            for item in supplies_list:
                values.append([item.cost, item.date])
        else: # alliws mono osa ikanopoioun ta filtra
            for item in supplies_list:
                if (str(item.date) >= first_date and str(item.date) <= last_date):
                    values.append([item.cost, item.date])


        #global total_rows
        #global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn eksodwn promitheiwn
        total_SupCost = 0
        for item in supplies_list:
            total_SupCost += item.getSupCost()

        #ypologismwn synolikwn eksodwn promitheiwn gia epilegmeno diastima
        total_SupCost_range = 0
        for item in values[1:]:
            if item:
                for j in range(total_columns-1):
                    total_SupCost_range += float(item[j])
            else:
                total_SupCost_range= total_SupCost

        total_SupCost =total_SupCost_range
            


        global records_list3
        records_list3=table.Table(sup_costs, total_rows, total_columns, values, total_SupCost)

        # button gia ta filtra sta supplies
        global filters_button3
        filters_button3 = Button(sup_costs, text="Filters", padx=100, fg="#4180fb", bg="#413c69",
                                activebackground="#413c69", activeforeground="#4180fb", command=open_filters)
        filters_button3.config(font=("Calibri", 24))
        filters_button3.grid(row=total_rows + 2, column=0, padx=20, pady=20, columnspan=3)


    def total_expenses():
        return total_opCost + total_salaries + total_SupCost
 
    def total_expenses_range():
        return total_opCost_range + total_salaries_month + total_SupCost_range
    

    #------------buttons-----------#

    # leitourgies gia ta buttons
    def open_filters():
        # dhmiourgia parathyrou
        global filters
        filters = Toplevel()
        filters.title("Filters")
        filters.iconbitmap("Images/budget_icon.ico")
        filters.configure(background="#4a47a3")

        # dhmiourgia frame gia Expenses
        types_frame = LabelFrame(filters, text="Expenses type", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
        types_frame.config(font=("Calibri", 20))
        types_frame.grid(row=0, column=0,padx=10, pady=10)

        variables_list = [] # lista me tis metavlhtes twn checkboxes
        for i in range(3):  #3 eidi expenses - OperatingCosts, Salaries, Supplies
            var = IntVar()
            variables_list.append(var)


        # dhmiourgia check buttons
        counter = -1
        for item in ["Operating Costs", "Salaries", "Supplies"]:
            counter += 1
            c = Checkbutton(types_frame, text=str(item), variable=variables_list[counter], bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
            c.config(font=("Calibri", 16))
            c.pack(anchor="w", padx=10)


        # dhmiourgia frame gia xroniko diasthma

        timerange_frame = LabelFrame(filters, text="Time Range", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
        timerange_frame.config(font=("Calibri", 20))
        timerange_frame.grid(row=0, column=1,padx=10, pady=10, columnspan=2)

        start_label = Label(timerange_frame, text="Starting Date or Select month for Salary", bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
        start_label.config(font=("Calibri", 16))
        start_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        start_input = Entry(timerange_frame, width=20)
        start_input.config(font=("Calibri", 16))
        start_input.grid(row=0, column=1, padx=10, pady=10)

        last_label = Label(timerange_frame, text="Last Date", bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
        last_label.config(font=("Calibri", 16))
        last_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        last_input = Entry(timerange_frame, width=20)
        last_input.config(font=("Calibri", 16))
        last_input.grid(row=1, column=1, padx=10, pady=10)



        #leitourgia apply button
        def apply_onclick():

            
            for i in range(len(variables_list)):
                if (variables_list[i].get() == 1):
                    if i==0:
                        for item in records_list1.cells_list:
                            item.destroy()
                        filters_button1.destroy()
                        create_table_Op_Costs(start_input.get(), last_input.get())
                    elif i==1:
                        for item in records_list2.cells_list:
                            item.destroy()
                        filters_button2.destroy()
                        filters_button4.destroy()
                        create_table_Salaries(start_input.get())
                    elif i==2:
                        for item in records_list3.cells_list:
                            item.destroy()
                        filters_button3.destroy()
                        create_table_Supplies(start_input.get(), last_input.get())


        # dhmiourgia apply button
        apply_button = Button(filters, text="Apply", fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=apply_onclick, padx=100)
        apply_button.grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=10)
        apply_button.config(font=("Calibri", 20))

    def open_salary():
        # dhmiourgia parathyrou
        global salary
        salary = Toplevel()
        salary.title("Change Salary")
        salary.iconbitmap("Images/budget_icon.ico")
        salary.configure(background="#4a47a3")

        # dhmiourgia frame gia allagi misthou

        salary_frame = LabelFrame(salary, text="", padx=10, pady=10, bg="#4a47a3", fg="#4180fb")
        salary_frame.config(font=("Calibri", 20))
        salary_frame.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        id_label = Label(salary_frame , text="Give Employee id ", bg="#4a47a3",
                            fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
        id_label .config(font=("Calibri", 16))
        id_label .grid(row=0, column=0, padx=10, pady=10, sticky="w")

        id_input = Entry(salary_frame, width=10)
        id_input.config(font=("Calibri", 16))
        id_input.grid(row=0, column=1, padx=10, pady=10)

        salary_label = Label(salary_frame, text="Set new salary ", bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3",
                           activeforeground="#4180fb")
        salary_label.config(font=("Calibri", 16))
        salary_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        salary_input = Entry(salary_frame, width=10)
        salary_input.config(font=("Calibri", 16))
        salary_input.grid(row=1, column=1, padx=10, pady=10)



        def apply_onclick():
            change_salary(id_input.get(),  salary_input.get())



        # dhmiourgia apply button
        apply_button = Button(salary, text="change", fg="#4180fb", bg="#413c69", activebackground="#413c69",
                              activeforeground="#4180fb", command=apply_onclick, padx=100)
        apply_button.grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=10)
        apply_button.config(font=("Calibri", 20))









    
