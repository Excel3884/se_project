from tkinter import *
import matplotlib.pyplot as plt
class Table:

    def __init__(self,root, total_rows, total_columns, values, total_income):
        self.cells_list = [] # xrhsimopoieitai gia na apothikuei ta kelia oste na nai eukolo na svhstoun argotera
        self.values = values
        # code for creating table
        for i in range(total_rows):
            height=0
            for j in range(total_columns):

                if (i == 0):
                    self.e = Entry(root, width=20, font=('Calibri', 16, 'bold'))
                    height=20
                    self.cells_list.append(self.e)
                else:
                    self.e = Entry(root, width=20,
                               font=('Calibri',16))
                    self.cells_list.append(self.e)


                if (j == 0):
                    self.e.grid(row=i, column=j, padx=(150, 0), pady=(height,0))
                elif (j == total_columns - 1):
                    self.e.grid(row=i, column=j, padx=(0, 20), pady=(height,0))
                else:
                    self.e.grid(row=i, column=j, pady=(height,0))

                self.e.insert(END, values[i][j])
                self.e.config(state="disabled")

        # telutaia grammh - total
        self.e = Entry(root, width=20, font=('Calibri', 16, 'bold'))
        self.cells_list.append(self.e)
        self.e.insert(END, "Total")
        self.e.config(state="disabled")
        self.e.grid(row=total_rows+1, column=0, padx=(150,0))

        self.e = Entry(root, font=('Calibri', 16))
        self.cells_list.append(self.e)
        self.e.grid(row=total_rows+1, column=1, columnspan=6, sticky="we", padx=(0,20))
        self.e.insert(END, str(total_income))
        self.e.config(state="disabled")

    # methodos gia dhmiourgia chart tou yparxontos table
    def make_chart(self):
        chart_data = {} # lexiko: date, income
        for record in self.values:
            if record[0] == "Id":
                pass
            else:
                if str(record[3]) not in chart_data.keys():
                    chart_data[str(record[3])] = record[4] * record[5]
                else:
                    chart_data[str(record[3])] += record[4] * record[5]

        plt.plot(chart_data.keys(), chart_data.values())
        plt.title("Sales - Line Chart")
        plt.xlabel("Date")
        plt.ylabel("Income")
        plt.show()
