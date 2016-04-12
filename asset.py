import csv
import sys
import operator
from datetime import datetime,timedelta

class StockIndex(object):
    def __init__(self, stock_file):
        self.stock_file = stock_file
        self.stock_lookup = {}
        self.readStocks()

# Read stock list and attributes from a CSV file
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
                        stock = CommonStock(symbol=symbol, last_div=last_div, par_value=par_value)
                    elif row['Type'] == 'Preferred':
                        stock = PrefStock(symbol=symbol, last_div=last_div, par_value=par_value, fixed_div=fixed_div)
                    self.stock_lookup[stock.symbol] = stock 

# Get a stock by symbol
    def get_stock(self, symbol):
        try:
            stock = self.stock_lookup[symbol]
        except KeyError:
            print "no stock for symbol %s" % symbol
            return None
        return stock

# Calculate the all share index
    def calculate_index(self):
        # Calculate geometric mean of  vol weighted stock prices for all stocks
        return (reduce(operator.mul, [r.get_vwsp() for r in self.stock_lookup.values()])) ** (1.0/len(self.stock_lookup))


# Simple trade report class
class TradeReport(object):
    def __init__(self, price, timestamp, side, volume):
        self.price = price
        self.timestamp = timestamp
        self.side = side
        self.volume = volume

    def __repr__(self):
        return '{}: {}, {}, {}, {}'.format(self.__class__.__name__,
                                        self.price,
                                        self.timestamp,
                                        self.side,
                                        self.volume)

## Stock super class
class Stock(object):
    def __init__(self):
        self.trades = []
        
    def get_div_yield(self, price):
        return (False, None)

    def get_pe_ratio(self, price):
        return (False, None)

    def get_vwsp(self):
        th = datetime.now() - timedelta(minutes = 5)
        num = sum([ float(r.price) * r.volume for r in self.trades if r.timestamp >= th ])
        denom = sum([ r.volume for r in self.trades if r.timestamp >= th ])
        return num/denom if denom > 0 else 0

    def record_trade(self, price, timestamp, side, volume):
        trade = TradeReport(price, timestamp, side, volume)
        self.trades.append(trade)
        return True


## Representation of a common stock
class CommonStock(Stock):
    def __init__(self, **kwargs):
        super(CommonStock, self).__init__()
        try:
            self.symbol = kwargs['symbol']
            self.last_div = kwargs['last_div']
            self.par_value = kwargs['par_value']
        except KeyError, e:
            sys.stderr.write('missing required arguments - "%s"\n' % str(e))

    def get_div_yield(self, price):
        return (True, float(self.last_div)/float(price))

    def get_pe_ratio(self, price):
        return (True, float(price)/float(self.last_div))


## Representation of a preferred stock
class PrefStock(Stock):
    def __init__(self, **kwargs):
        super(PrefStock, self).__init__()
        try:
            self.symbol = kwargs['symbol']
            self.last_div = kwargs['last_div']
            self.par_value = kwargs['par_value']
            self.fixed_div = kwargs['fixed_div']
        except KeyError, e:
            sys.stderr.write('missing required arguments - "%s"\n' % str(e))

    def get_div_yield(self, price):
        return (True, float(self.fixed_div)/100*float(self.par_value)/float(price))

    def get_pe_ratio(self, price):
        return (True, float(price)/(float(self.fixed_div)/100*float(self.par_value)))
