import csv

class StockFactory(object):
    def __init__(self, stock_file):
        self.stock_file = stock_file
        self.stock_lookup = {}
        self.readStocks()

    def readStocks(self):
        with open(self.stock_file, 'r') as f:
            stocks = csv.reader(f, delimiter=',')
            header=None
            for r in stocks:
                if header == None:
                    header = r
                else:
                    row = dict(zip(header, r))
                    symbol = row['Stock Symbol']
                    last_div=row['Last Dividend']
                    par_value=row['Par Value']
                    fixed_div=row['Fixed Dividend']
                    if row['Type'] == 'Common':
                        stock = Stock(sym=symbol, last_div=last_div, par_value=par_value)
                    elif row['Type'] == 'Preferred':
                        stock = PrefStock(sym=symbol, last_div=last_div, par_value=par_value, fixed_div=fixed_div)
                    self.stock_lookup[stock.symbol] = stock 

    def get_stock(self, symbol):
        try:
            stock = self.stock_lookup[symbol]
        except KeyError:
            print "no stock for symbol %s" % symbol
            return None
        return stock

## Representation of a basic ordinary 'stock'
class Stock(object):
    def __init__(self, **kwargs):
        try:
            self.symbol = kwargs['sym']
            self.last_div = kwargs['last_div']
            self.par_value = kwargs['par_value']
        except:
            pass

    def get_div_yield(self, price):
        return (True, float(self.last_div)/float(price))

    def get_pe_ratio(self, price):
        return (True, float(price)/float(self.last_div))

    def get_vwsp(self):
        return 0

    def record_trade(self, price, timestamp, side, volume):
        pass

## Representation of a preferred stock
class PrefStock(Stock):
    def __init__(self, **kwargs):
        try:
            self.symbol = kwargs['sym']
            self.last_div = kwargs['last_div']
            self.par_value = kwargs['par_value']
            self.fixed_div = kwargs['fixed_div']
        except:
            pass

    def get_div_yield(self, price):
        return (True, float(self.fixed_div)/100*float(self.par_value)/float(price))

    def get_pe_ratio(self, price):
        return (True, float(price)/(float(self.fixed_div)/100*float(self.par_value)))

    def get_vwsp(self):
        return 0

    def record_trade(self, price, timestamp, side, volume):
        pass