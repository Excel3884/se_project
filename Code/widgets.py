from tkinter import *
import dbConnection
import matplotlib.pyplot as plt
import single_sale as ss # periexei thn klash Sale
import plotly.graph_objects as go
import plotly
import plotly.io as pio
from PIL import Image, ImageDraw, ImageFont

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

        #metatroph titlou se eikona gia th xrhsh tou os widget

        # onoma tou arxeiou gia apothikeush
        filename = "widget_title.png"
        fnt = ImageFont.truetype("cambriab.ttf", 28)
        #dhmiourgia eikonas
        image = Image.new(mode = "RGB", size = (600,50), color = "white")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), title, font=fnt, fill="black")
        image.save(filename)



    def get_chart(self):

        if self.chart_option == 0:
            pass
        else:

            #sundesh sth vash dedomenwn
            conn = dbConnection.conn

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
            self.filtered_sales = [] #lista me ta telika proionta
            for item in sales_list:
                if (str(item.prod_date) >= self.start_date and str(item.prod_date) <= self.last_date):
                    self.filtered_sales.append(item)

            #lexiko me type, pwlhseis
            chart_data = {}
            #arxikopoihsh
            for item in self.chosen_types:
                chart_data[str(item)] = 0
            #eisagwgh timwn
            for item in self.filtered_sales:
                chart_data[str(item.prod_type)] += item.prod_amount



            data = list(chart_data.values())
            labels = list(chart_data.keys())
            plt.pie(data, labels=labels)
            plt.title("Sales Allocation")


            plt.savefig('widget_pie.jpg',bbox_inches='tight', dpi=150)
            plt.close('all')



    # def get_table(self):
    #     # pinakas: name, type , amount, income, purchase
    #     names_column = []
    #     type_column = []
    #     amount_column = []
    #     income_column = []
    #     purchase_column = []
    #     for item in self.filtered_sales:
    #         names_column.append(item.prod_name)
    #         type_column.append(item.prod_type)
    #         amount_column.append(item.prod_amount)
    #         income_column.append(item.get_income)
    #         purchase_column.append(item.prod_purchase)


    #     summary_tb = go.Figure(data=[go.Table(
    # header=dict(values=["Name", "Type", "Amount", "Income", "Purchase"],
    #             line_color='darkslategray',
    #             fill_color='lightskyblue',
    #             align='left'),
    # cells=dict(values=[names_column, # 1st column
    #                    type_column, # 2nd column
    #                    amount_column, # 3rd column
    #                    income_column, # 4th column
    #                    purchase_column], # 5th column
    #            line_color='darkslategray',
    #            fill_color='lightcyan',
    #            align='left'))
# ])
    #     summary_tb.update_layout(width=500, height=300)
    #     # summary_tb.write_image("summary_tb.png")
    #     pio.write_image(summary_tb, "summary_tb.png")

    def order_list(self):
        # taxinomhsh twn sales se fthinousa seira me vash tis pwlhseis
        # gia na paroume ta proionta me tis perissoteres pwlhseis
        self.filtered_sales.sort(key=lambda x: x.prod_amount, reverse=True)
        order_list = "Top 2 selling products to be ordered: \n"
        order_list += "1. " + str(self.filtered_sales[0].prod_name) + "\n"
        order_list += "2. " + str(self.filtered_sales[1].prod_name)

        #metatroph order_list se eikona gia th xrhsh tou os widget

        # onoma tou arxeiou gia apothikeush
        filename = "widget_orders.png"
        fnt = ImageFont.truetype("arial.ttf", 20)
        #dhmiourgia eikonas
        image = Image.new(mode = "RGB", size = (600,200), color = "white")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), order_list, font=fnt, fill="black")
        image.save(filename)








