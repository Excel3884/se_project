from tkinter import *
import mysql.connector
import matplotlib.pyplot as plt
import single_sale as ss # periexei thn klash Sale

class Widgets(): # h klash einai mono gia pwlhseis afou auto einai to senario sta use cases

    def __init__(self, sales_option, expenses_option, selected_products, products_variables, start_date, last_date, chart_option):

        self.sales_option = sales_option
        self.expenses_option = expenses_option
        self.selected_products = selected_products # lista twn proiontwn gia antistoixish me ta variables(epilogwn)
        self.products_variables = products_variables
        self.start_date = start_date
        self.last_date = last_date
        self.chart_option = chart_option
        self.chosen_types = [] # eidh proiontwn pou tha epilexei o xrhsths


    def get_title(self):

        title = "Products: "
        first = True
        for i in range(len(self.selected_products)):
            if self.products_variables[i].get() == 1:
                self.chosen_types.append(self.selected_products[i]) # h lista tha xrhsimopoih8ei sth methodo get_chart
                if first == False:
                    title += ", "
                else:
                    first = False

                title += str(self.selected_products[i])

        return title



    def get_chart(self):

        if self.chart_option == 0:
            pass
        else:

            #sundesh sth vash dedomenwn
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="fundanalyst"
            )

            cur = conn.cursor()
            global sales_list
            sales_list = [] # lista me tis pwlhseis ws objects

            # anakthsh pwlhsewn pou antistoixoun sta eidh pou epelexe o xrhsths
            query = "SELECT * FROM sales WHERE type IN ({c})".format(c=', '.join(['%s']*len(self.chosen_types)))
            cur.execute(query, self.chosen_types)
            rows = cur.fetchall()
            for row in rows:
                object_row = ss.Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                sales_list.append(object_row)


            #filtrarisma pwlhsewn gia na paroume autes pou antistoixoun sto orismeno xroniko diasthma
            filtered_sales = [] #lista me ta telika proionta
            for item in sales_list:
                if (str(item.prod_date) >= self.start_date and str(item.prod_date) <= self.last_date):
                    filtered_sales.append(item)

            #lexiko me type, pwlhseis
            chart_data = {}
            #arxikopoihsh
            for item in self.chosen_types:
                chart_data[str(item)] = 0
            #eisagwgh timwn
            for item in filtered_sales:
                chart_data[str(item.prod_type)] += item.prod_amount



            data = list(chart_data.values())
            labels = list(chart_data.keys())
            plt.pie(data, labels=labels)
            plt.title("Sales Allocation")


            plt.savefig('pie.jpg',bbox_inches='tight', dpi=150)



    def get_table(self):
        pass

    def order_list(self):
        pass
