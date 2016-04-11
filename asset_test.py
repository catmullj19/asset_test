import unittest
from asset import *

class CommonStockDividendYieldTest(unittest.TestCase):
    def setUp(self):
        self.test_stock_factory = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_factory.get_stock('POP')
        #self.test_stock_prf = self.test_stock_factory.get_stock('GIN')

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
        self.test_stock_factory = StockIndex('test_stocks.csv')
        self.test_stock_prf = self.test_stock_factory.get_stock('GIN')

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
        self.test_stock_factory = StockIndex('test_stocks.csv')
        self.test_stock_com = self.test_stock_factory.get_stock('POP')

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
        self.test_stock_factory = StockIndex('test_stocks.csv')
        self.test_stock_prf = self.test_stock_factory.get_stock('GIN')

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

if __name__ == '__main__':

    unittest.TextTestRunner(verbosity=2).run(div_yield_suite())
    unittest.TextTestRunner(verbosity=2).run(pe_ratio_suite())
