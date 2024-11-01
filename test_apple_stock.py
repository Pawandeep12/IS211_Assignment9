import unittest
from apple_stock import parse_apple_stock

class TestAppleStock(unittest.TestCase):
    def test_parse_apple_stock(self):
        results = parse_apple_stock()
        # Check if the results list is not empty
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        # Check the structure of the first result
        if results:
            first_data = results[0]
            self.assertIn("date", first_data)
            self.assertIn("close_price", first_data)

if __name__ == '__main__':
    unittest.main()
