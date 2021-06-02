import Employee
import Operating_Cost
import Supply

import  mysql.connector

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
    expenses_costs.iconbitmap("Images/Sales_icon.ico")
    expenses_costs.configure(background="#4a47a3")
    expenses_costs.state("zoomed")

    #---------lista eggrafwn-----------#


    class Expenses(Employee, Operating_Cost, Supplies):

        def __init__(self):
            self.outcome = 0





    Op_Costs_list = [] # lista me ta eksoda leitoyrgias ws objects
    
    cur.execute("SELECT * FROM operatingCosts")
    rows = cur.fetchall()
    for row in rows:
        object_row = Operating_Cost(row[0], row[1], row[2], row[3], row[4]) 
        Op_Costs_list.append(object_row)

    
    #------------dhmiourgia pinaka--------------#
    def create_table_Op_Costs(first_date, last_date):

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
            total_opCost_range += item.get_Operating_Costs()
            

        global records_list
        records_list = table.Table(expenses_costs, total_rows, total_columns, values, total_opCost)
        
    create_table_Op_Costs('', '')



    employees_list = [] # lista me ta eksoda misthwn ypallilwn

    cur.execute("SELECT * FROM Employees")
    rows = cur.fetchall()
    for row in rows:
        object_row = Employee(row[0], row[1], row[2], row[3], row[4])
        employees_list.append(object_row)

    #------------dhmiourgia pinaka--------------#
    def create_table_Salaries(month):

        values = []
        values.append(["Name", "Lastname", "ID", "Salary", "Month"])
        if len(month) == 0 : # an den dinetai minas prosthese oles tis eggrafes
            for item in employees_list:
                values.append([item.name, item.lastname, item.id, item.salary, item.month])
        else: # alliws mono tous misthous tou mina pou dothike
            for item in employees_list:
                if (str(item.month) == month):
                    values.append([item.name, item.lastname, item.id, item.salary, item.month])


        global total_rows
        global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn eksodwn
        total_salaries = 0
        for item in employees_list:
            total_salaries += item.getSalary()

        #ypologismwn synolikwn eksodwn gia epilegmeno diastima
        total_salaries_month = 0
        for item in values[1:]:
            total_salaries_month += item.getSalary()


        #    global records_list
        records_list = table.Table(expenses_costs, total_rows, total_columns, values, total_salaries)

    create_table_Salaries('')


    def change_salary(id, month, new_salary):
        for item in employees_list:
            if item.getID()==id and item.getMonth()==month :
                item.setSalary(new_salary)
                cur.execute("UPDATE Employees SET Salary=%s WHERE ID=%s AND month=%s", str(new_salary), str(id), str(month))

          
    change_salary('', '', '')




    supplies_list = [] # lista me ta eksoda promitheiwn

    cur.execute("SELECT * FROM Supplies")
    rows = cur.fetchall()
    for row in rows:
        object_row = Supplies(row[0], row[1])
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


        global total_rows
        global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn eksodwn promitheiwn
        total_SupCost = 0
        for item in supplies_list:
            total_SupCost += item.getSupCost()

        #ypologismwn synolikwn eksodwn promitheiwn gia epilegmeno diastima
        total_SupCost_range = 0
        for item in values[1:]:
            total_SupCost_range += item.getSupCost()
            

         #   global records_list
        records_list = table.Table(expenses_costs, total_rows, total_columns, values, total_SupCost)
        
    create_table_Supplies('', '')


    def total_expenses():
        return total_opCost + total_salaries + total_SupCost
 
    def total_expenses_range():
        return total_opCost_range + total_salaries_month + total_SupCost_range
    

    #------------buttons-----------#

    # leitourgies gia ta buttons
    def open_filters():
        # dhmiourgia parathyrou
        filters = Toplevel()
        filters.title("Filters")
        filters.iconbitmap("Images/expenses_icon.ico")
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

            # diagrafh prohgoumenou pianaka
            for item in records_list.cells_list:
                item.destroy()
                
            
            for i in range(len(variables_list)):
                if (variables_list[i].get() == 1):
                    if i==1:
                        create_table_Op_Costs(start_input.get(), last_input.get())
                    elif i==2:
                        create_table_Salaries(start_input.get()[1])  #check if valid (method returns list, combine method call with index)
            


        # dhmiourgia apply button
        apply_button = Button(filters, text="Apply", fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=apply_onclick, padx=100)
        apply_button.grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=10)
        apply_button.config(font=("Calibri", 20))


    def open_chart():
        records_list.make_chart()

    # button gia ta filtra
    filters_button = Button(expenses_costs, text="Filters", padx=100, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_filters)
    filters_button.config(font=("Calibri", 24))
    filters_button.grid(row=total_rows+2, column=0, padx=20, pady=20, columnspan=3)

    # button gia to grafhma
    chart_button = Button(expenses_costs, text="Chart", padx=100, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_chart)
    chart_button.config(font=("Calibri", 24))
    chart_button.grid(row=total_rows+2, column=4, padx=20, pady=20, columnspan=3)



    
