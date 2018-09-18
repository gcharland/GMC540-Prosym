class Company(object):
    money = 0
    employees = 0
    base_material = 0
    month = 1

    def __init__(self, money, employees, base_material, month):
        self.money = money
        self.employees = employees
        self.base_material = base_material
        self.month = month

    def buy(self, provider, volume):
        while volume > provider.vol_max:
            print("Volume demandé trop grand, veuillez commander maximum " + str(provider.vol_max))
            volume = int(input("Quel volume souhaitez-vous commander?: "))

        print("Achat de " + str(volume) + "PPM au " + str(self.month) + "em mois")

        unit_price = provider.get_price(volume, self.month)
        print("Prix unitaire de " + str(unit_price) + "$")
        print("Frais fixes de " + str(provider.initial_cost) + "$")
        print("Dépense de " + str(unit_price*volume + provider.initial_cost) + "$")
        self.money -= unit_price*volume + provider.initial_cost
        self.base_material += volume
