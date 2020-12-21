import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
	def test_getDataPoint_calculatePrice(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
			]
		for quote in quotes:
			self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		quotes = [
			{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
			]
		for quote in quotes:
			self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))
	
	def test_getRatio_calculateRatio(self):
		prices = {
			'ABC': 114.25,
			'DEF': 112.035
			}
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), prices['ABC']/prices['DEF'])
	
	def test_getRatio_calculateRatioPriceAZero(self):
		prices = {
			'ABC': 0,
			'DEF': 112.035
			}
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), 0)
	
	def test_getRatio_calculateRatioPriceBZero(self):
		prices = {
			'ABC': 114.25,
			'DEF': 0
			}
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), None)

if __name__ == '__main__':
	unittest.main()
