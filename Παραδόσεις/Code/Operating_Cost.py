

class Operating_Cost():

    def __init__(self, reyma, nero, tilefono, rent, date):
        self.reyma = reyma
        self.nero = nero
        self.tilefono = tilefono
        self.rent = rent
        self.date = date

   # def set_store_id(self, store_id):
            #self.store_id = store_id

    def set_reyma(self, reyma):
        self.reyma = reyma
            
    def set_nero(self, nero):
        self.nero = nero
    def set_tilefono(self, tilefono):
        self.tilefono = tilefono
    def set_rent(self, rent):
        self.rent = rent

    def get_Operating_Costs(self):
        return self.reyma + self.nero + self.tilefono + self.rent

    
