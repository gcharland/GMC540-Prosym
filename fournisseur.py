class Fournisseur(object):
    vol_max = 0
    delay = 0
    initial_cost = 0
    price_list = []
    quality_stats = []

    def __init__(self, vol_max, delay, initial_cost, price_list, quality_stats):
        self.vol_max = vol_max
        self.delay = delay
        self.initial_cost = initial_cost
        self.price_list = price_list
        self.quality_stats = quality_stats

        for i in range(0, len(price_list)):
            for j in range(0, len(price_list[i])):
                price_list[i][j] = float(price_list[i][j])

    def get_price(self, asked_volume, month):
        delimiters = self.price_list[0]

        price_column = 0
        while asked_volume >= delimiters[price_column]:
            price_column += 1

        return self.price_list[month][price_column]
