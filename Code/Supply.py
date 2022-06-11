

class Supply():
    def __init__(self, id, cost, date):
        self.id = id
        self.cost = cost
        self.date = date

    def getSupCost(self):
        return float(self.cost)
