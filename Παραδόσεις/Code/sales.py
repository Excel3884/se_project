from tkinter import *
import  mysql.connector
import table
import single_sale #periexei thn klash Sale

# sundesh sth vash dedomenwn
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fundanalyst"
)

cur = conn.cursor()



def SalesWindow():
    # dhmiourgia parathyrou
    sales = Toplevel()
    sales.title("Sales")
    sales.iconbitmap("Images/budget_icon.ico")
    sales.configure(background="#4a47a3")
    sales.state("zoomed")

    #---------lista eggrafwn-----------#

    sales_list = [] # lista me tis pwlhseis ws objects

    cur.execute("SELECT * FROM sales")
    rows = cur.fetchall()
    for row in rows:
        object_row = single_sale.Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        sales_list.append(object_row)



    prod_types = [] # lista me ta product types

    # dhmiourgia listas
    for item in sales_list:
        if item.prod_type not in prod_types:
            prod_types.append(item.prod_type)


    #------------dhmiourgia pinaka--------------#
    def create_table(selected_types, first_date, last_date):

        values = []
        values.append(["Id", "Name", "Type", "Date", "Price", "Amount", "Purchase"])
        if len(first_date) == 0 or len(last_date) == 0: # an toulaxiston ena entry einai adeio des mono ta filtra twn types
            for item in sales_list:
                if (item.prod_type in selected_types):
                    values.append([item.prod_id, item.prod_name, item.prod_type, item.prod_date, item.prod_price, item.prod_amount, item.prod_purchase])
        else: # alliws des ola ta filtra
            for item in sales_list:
                if (item.prod_type in selected_types) and (str(item.prod_date) >= first_date and str(item.prod_date) <= last_date):
                    values.append([item.prod_id, item.prod_name, item.prod_type, item.prod_date, item.prod_price, item.prod_amount, item.prod_purchase])


        global total_rows
        global total_columns
        total_rows = len(values)
        total_columns = len(values[0])

        #ypologismwn synolikwn esodwn
        total_income = 0
        for item in sales_list:
            if item.prod_type in selected_types:
                total_income += item.get_income()


        global records_list
        records_list = table.Table(sales, total_rows, total_columns, values, total_income)

    create_table(prod_types, '', '')





    #------------buttons-----------#

    # leitourgies gia ta buttons
    def open_filters():
        # dhmiourgia parathyrou
        filters = Toplevel()
        filters.title("Filters")
        filters.iconbitmap("Images/budget_icon.ico")
        filters.configure(background="#4a47a3")

        # dhmiourgia frame gia product types
        types_frame = LabelFrame(filters, text="Product type", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
        types_frame.config(font=("Calibri", 20))
        types_frame.grid(row=0, column=0,padx=10, pady=10)

        variables_list = [] # lista me tis metavlhtes twn checkboxes
        for i in range(len(prod_types)):
            var = IntVar()
            variables_list.append(var)


        # dhmiourgia check buttons
        counter = -1
        for item in prod_types:
            counter += 1
            c = Checkbutton(types_frame, text=str(item), variable=variables_list[counter], bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
            c.config(font=("Calibri", 16))
            c.pack(anchor="w", padx=10)


        # dhmiourgia frame gia xroniko diasthma

        timerange_frame = LabelFrame(filters, text="Time Range", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
        timerange_frame.config(font=("Calibri", 20))
        timerange_frame.grid(row=0, column=1,padx=10, pady=10, columnspan=2)

        start_label = Label(timerange_frame, text="Starting Date", bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
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
            selected_types = [] # lista me epilegmena dedomena gia provolh
            for i in range(len(variables_list)):
                if (variables_list[i].get() == 1):
                    selected_types.append(prod_types[i])

            # diagrafh prohgoumenou pianaka
            for item in records_list.cells_list:
                item.destroy()

            #dhmiourgia neou
            create_table(selected_types, start_input.get(), last_input.get())


        # dhmiourgia apply button
        apply_button = Button(filters, text="Apply", fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=apply_onclick, padx=100)
        apply_button.grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=10)
        apply_button.config(font=("Calibri", 20))




    def open_chart():
        records_list.make_chart()


    # button gia ta filtra
    filters_button = Button(sales, text="Filters", padx=100, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_filters)
    filters_button.config(font=("Calibri", 24))
    filters_button.grid(row=total_rows+2, column=0, padx=20, pady=20, columnspan=3)



    # button gia to grafhma
    chart_button = Button(sales, text="Chart", padx=100, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_chart)
    chart_button.config(font=("Calibri", 24))
    chart_button.grid(row=total_rows+2, column=4, padx=20, pady=20, columnspan=3)
