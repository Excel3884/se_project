from tkinter import *
import mysql.connector
import widgets #klash gia dhmiourgia widgets gia thn anafora

#sundesh sth vash dedomenwn
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fundanalyst"
)

cur = conn.cursor()

#parathyro gia epiloegh dedomenwn(sales/expenses)
def ReportWindow():
    #dhmiourgia parathyrou erwthshs dedomenwn
    report_data = Toplevel()
    report_data.title("Create Report")
    report_data.iconbitmap("Images/budget_icon.ico")
    report_data.configure(background="#4a47a3")

    #frame me tis epiloges pwlhseis/exoda
    data_frame = LabelFrame(report_data, text="Data to be used", padx=10, pady=10, bg="#4a47a3", fg="#4180fb")
    data_frame.config(font=("Calibri", 20))
    data_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")

    #metavlhtes gia ta checkbuttons
    global sales_var
    sales_var = IntVar()
    global expenses_var
    expenses_var = IntVar()

    #checkbuttons
    sales_check = Checkbutton(data_frame, text="Sales", variable=sales_var, bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
    sales_check.config(font=("Calibri", 16))
    sales_check.grid(row=0, column=0, sticky="w")

    expenses_check = Checkbutton(data_frame, text="Expenses", variable=expenses_var, bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
    expenses_check.config(font=("Calibri", 16))
    expenses_check.grid(row=1, column=0, sticky="w")


    #leitourgies gia ta buttons
    def close_report_data():
        report_data.destroy()

    def open_filters():
        report_data.destroy()
        openFilters()


    #buttons
    cancel_button = Button(report_data, text="Cancel", command=close_report_data, padx=50,fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb")
    cancel_button.grid(row=1, column=0, padx=10, pady=10)
    cancel_button.config(font=("Calibri", 16))


    next_button = Button(report_data, text="Next", command=open_filters, padx=50, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb")
    next_button.grid(row=1, column=1, padx=10, pady=10)
    next_button.config(font=("Calibri", 16))


# anakthsh eidwn proiontwn
def get_types():
    all_types = []
    cur.execute("SELECT type FROM sales")
    rows = cur.fetchall()
    for row in rows:
        all_types.append(row[0])

    # dhmiourgia listas me kathe eidos mono mia fora
    types = []

    for item in all_types:
        if item not in types:
            types.append(item)

    return types

#parathyro me ta filtra
def openFilters():
    #dhmiourgia parathyrou
    report_filters = Toplevel()
    report_filters.title("Create Report - Filters")
    report_filters.iconbitmap("images/budget_icon.ico")
    report_filters.configure(background="#4a47a3")

    global prod_types
    prod_types = get_types()

    # dhmiourgia frame gia product types
    types_frame = LabelFrame(report_filters, text="Product type", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
    types_frame.config(font=("calibri", 20))
    types_frame.grid(row=0, column=0,padx=10, pady=10)


    global variables_list
    variables_list = [] # lista me tis metavlhtes twn checkboxes
    for i in range(len(prod_types)):
        var = IntVar()
        variables_list.append(var)


    # dhmiourgia check buttons
    counter = -1
    for item in prod_types:
        counter += 1
        c = Checkbutton(types_frame, text=str(item), variable=variables_list[counter], bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
        c.config(font=("calibri", 16))
        c.pack(anchor="w", padx=10)


    #frame gia xroniko diasthma

    timerange_frame = LabelFrame(report_filters, text="Time Range", padx=10, pady=10,bg="#4a47a3", fg="#4180fb")
    timerange_frame.config(font=("Calibri", 20))
    timerange_frame.grid(row=0, column=1,padx=10, pady=10)

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


    #leitourgies gia ta buttons
    def close_report_filters():
        report_filters.destroy()

    def open_charts():
        global start_date
        start_date = start_input.get() #apothikeush pediou prwths hmeromhnias
        global last_date
        last_date = last_input.get() #apothikeush pediou teleutaias hmeromhnias
        f_date = start_input.get()

        report_filters.destroy()
        openCharts()



    #buttons
    cancel_button = Button(report_filters, text="Cancel", padx=50,fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=close_report_filters)
    cancel_button.grid(row=1, column=0, padx=10, pady=10)
    cancel_button.config(font=("Calibri", 16))


    next_button = Button(report_filters, text="Next", padx=50, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_charts)
    next_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
    next_button.config(font=("Calibri", 16))

def openCharts():

    #dhmiourgia parathyrou
    report_charts = Toplevel()
    report_charts.title("Create Report - Charts")
    report_charts.iconbitmap("images/budget_icon.ico")
    report_charts.configure(background="#4a47a3")

    #epikefalida
    choose_label = Label(report_charts, text="Chart:", bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
    choose_label.config(font=("Calibri", 18))
    choose_label.grid(row=0, column=0, padx=10, sticky="w", columnspan=2)


    #checkboxes
    global chart_option
    chart_option = IntVar()

    chart_histogram = Radiobutton(report_charts, text="Histogram", variable=chart_option, value=0, bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
    chart_histogram.config(font=("calibri", 16))
    chart_histogram.grid(row=1, column=0, columnspan=2,sticky="w", padx=10)


    chart_pie = Radiobutton(report_charts, text="Pie", variable=chart_option, value=1, bg="#4a47a3", fg="#4180fb", activebackground="#4a47a3", activeforeground="#4180fb")
    chart_pie.config(font=("calibri", 16))
    chart_pie.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)


    #leitourgies gia ta buttons
    def close_report_charts():
        report_charts.destroy()

    def open_create_report():
        report_charts.destroy()
        openCreateReport()



    #buttons
    cancel_button = Button(report_charts, text="Cancel", padx=50,fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=close_report_charts)
    cancel_button.grid(row=3, column=0, padx=10, pady=10)
    cancel_button.config(font=("Calibri", 16))


    next_button = Button(report_charts, text="Next", padx=50, fg="#4180fb", bg="#413c69", activebackground="#413c69", activeforeground="#4180fb", command=open_create_report)
    next_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")
    next_button.config(font=("Calibri", 16))


    def openCreateReport():

        #dhmiourgia antikeimenou typou Widgets
        report_widgets = widgets.Widgets(sales_var, expenses_var, prod_types, variables_list, start_date, last_date, chart_option)

        #report title
        report_title = report_widgets.get_title()

        #report chart
        report_widgets.get_chart()

        #report summary-table

        #products to be ordered due to demand






