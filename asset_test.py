import sys
import unittest
from datetime import datetime,timedelta

from asset import *

class CommonStockDividendYieldTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_index.get_stock('POP')

    def tearDown(self):
        pass

    def test_get_com_div_yield(self):
        test_price = float(99.9)
        test_yield = 8/test_price
        status, yld = self.test_stock_com.get_div_yield(test_price)
        self.assertEqual(status, True)
        self.assertEqual(yld, test_yield)

    def __str__(self):
        return 'CommonStockDividendYieldTest'

class PrefStockDividendYieldTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_prf = self.test_stock_index.get_stock('GIN')

    def tearDown(self):
        pass

    def test_get_prf_div_yield(self):
        test_price = float(199.9)
        test_yield = 100*.02/test_price
        status, yld = self.test_stock_prf.get_div_yield(test_price)
        self.assertEqual(status, True)
        self.assertEqual(yld, test_yield)

    def __str__(self):
        return 'PrefStockDividendYieldTest'

class CommonStockPERatioTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_index.get_stock('POP')

    def tearDown(self):
        pass

    def test_get_com_pe_ratio(self):
        test_price = 99.9
        test_pe_ratio = test_price/8
        status, pe_ratio = self.test_stock_com.get_pe_ratio(test_price)
        self.assertEqual(status, True)
        self.assertEqual(pe_ratio, test_pe_ratio)

    def __str__(self):
        return 'CommonStockPERatioTest'

class PrefStockPERatioTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_prf = self.test_stock_index.get_stock('GIN')

    def tearDown(self):
        pass

    def test_get_prf_pe_ratio(self):
        test_price = 299.9
        test_pe_ratio = test_price/(100*0.02)
        status, pe_ratio = self.test_stock_prf.get_pe_ratio(test_price)
        self.assertEqual(status, True)
        self.assertEqual(pe_ratio, test_pe_ratio)

    def __str__(self):
        return 'PrefStockPERatioTest'

class CommonStockTradeTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_index.get_stock('POP')

    def tearDown(self):
        pass

    def test_common_stock_trade(self):
        test_price = 299.9
        test_volume = 5000
        test_side = 'B'
        test_timestamp = datetime.strptime("30/03/16 10:30:01", "%d/%m/%y %H:%M:%S")
        status = self.test_stock_com.record_trade(test_price, test_timestamp, test_side, test_volume)
        self.assertEqual(status, True)

    def __str__(self):
        return 'CommonStockTradeTest'

class CommonStockVWSPTest(unittest.TestCase):
    
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_index.get_stock('POP')

    def tearDown(self):
        pass

    def test_common_stock_vswp(self):
        test_price = 299.9
        test_volume = 5000
        test_side = 'B'
        test_timestamp = datetime.now() - timedelta(seconds=50)
        self.test_stock_com.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 299.1
        test_volume = 10000
        test_side = 'S'
        test_timestamp = datetime.now() - timedelta(seconds=40)
        self.test_stock_com.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 300
        test_volume = 500
        test_side = 'B'
        test_timestamp = datetime.now() - timedelta(seconds=30)
        self.test_stock_com.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 289.9
        test_volume = 50000
        test_side = 'S'
        test_timestamp = datetime.now() - timedelta(seconds=301)
        self.test_stock_com.record_trade(test_price, test_timestamp, test_side, test_volume)

        test_vwsp = self.test_stock_com.get_vwsp()
        self.assertAlmostEqual(test_vwsp, 299.3870968)

    def __str__(self):
        return 'CommonStockVWSPTest'

class PrefStockVWSPTest(unittest.TestCase):
    
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stock_pref = self.test_stock_index.get_stock('GIN')

    def tearDown(self):
        pass

    def test_pref_stock_vswp(self):
        test_price = 300
        test_volume = 10
        test_side = 'S'
        test_timestamp = datetime.now() - timedelta(seconds=50)
        self.test_stock_pref.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 301
        test_volume = 20
        test_side = 'B'
        test_timestamp = datetime.now() - timedelta(seconds=40)
        self.test_stock_pref.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 302
        test_volume = 50
        test_side = 'B'
        test_timestamp = datetime.now() - timedelta(seconds=30)
        self.test_stock_pref.record_trade(test_price, test_timestamp, test_side, test_volume)
        test_price = 300
        test_volume = 500
        test_side = 'S'
        test_timestamp = datetime.now() - timedelta(seconds=301)
        self.test_stock_pref.record_trade(test_price, test_timestamp, test_side, test_volume)

        test_vwsp = self.test_stock_pref.get_vwsp()
        self.assertAlmostEqual(test_vwsp, 301.5)

    def __str__(self):
        return 'PrefStockVWSPTest'

class StockIndexTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_index = StockIndex('test_stocks.csv')
        self.test_stocks = []
        self.test_stocks.append(self.test_stock_index.get_stock('TEA'))
        self.test_stocks.append(self.test_stock_index.get_stock('POP'))
        self.test_stocks.append(self.test_stock_index.get_stock('ALE'))
        self.test_stocks.append(self.test_stock_index.get_stock('GIN'))
        self.test_stocks.append(self.test_stock_index.get_stock('JOE'))

    def tearDown(self):
        pass

    def test_stock_index(self):
        # record trades to create some prices
        for s in self.test_stocks:
            s.record_trade(100, datetime.now(), 'B', 10)

        index_val = self.test_stock_index.calculate_index()
        self.assertAlmostEqual(index_val, 100)

    def __str__(self):
        return 'StockIndexTest'

def div_yield_suite():
    suite = unittest.TestSuite()
    suite.addTest(CommonStockDividendYieldTest('test_get_com_div_yield'))
    suite.addTest(PrefStockDividendYieldTest('test_get_prf_div_yield'))
    return suite

def pe_ratio_suite():
    suite = unittest.TestSuite()
    suite.addTest(CommonStockPERatioTest('test_get_com_pe_ratio'))
    suite.addTest(PrefStockPERatioTest('test_get_prf_pe_ratio'))
    return suite

def trade_suite():
    suite = unittest.TestSuite()
    suite.addTest(CommonStockTradeTest('test_common_stock_trade'))
    return suite

def vswp_suite():
    suite = unittest.TestSuite()
    suite.addTest(CommonStockVWSPTest('test_common_stock_vswp'))
    suite.addTest(PrefStockVWSPTest('test_pref_stock_vswp'))
    return suite
    
def index_suite():
    suite = unittest.TestSuite()
    suite.addTest(StockIndexTest('test_stock_index'))
    return suite
    
if __name__ == '__main__':

    sys.stdout.write('\n\n********************\n')
    sys.stdout.write('** Starting Tests **\n')
    sys.stdout.write('********************\n\n')
    unittest.TextTestRunner(verbosity=2).run(div_yield_suite())
    unittest.TextTestRunner(verbosity=2).run(pe_ratio_suite())
    unittest.TextTestRunner(verbosity=2).run(trade_suite())
    unittest.TextTestRunner(verbosity=2).run(vswp_suite())
    unittest.TextTestRunner(verbosity=2).run(index_suite())
    
    
    
