import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    dummyResponse1 = ('ABC', 120.48, 121.2, 120.84)
    dummyResponse2 = ('DEF', 117.87, 121.68, 119.775)
    self.assertEqual(getDataPoint(quotes[0]), dummyResponse1)
    self.assertEqual(getDataPoint(quotes[1]), dummyResponse2)
    

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    dummyResponse = ('ABC', 120.48, 119.2, 119.84)
    self.assertEqual(getDataPoint(quotes[0]), dummyResponse)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_divison_by_zero(self):
    price1 = 120.48
    price2 = 0
    self.assertRaises(ZeroDivisionError, getRatio, price1, price2)


if __name__ == '__main__':
    unittest.main()
