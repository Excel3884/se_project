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

