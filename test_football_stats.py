import unittest
from football_stats import parse_football_stats

class TestFootballStats(unittest.TestCase):
    def test_parse_football_stats(self):
        results = parse_football_stats()
        # Check if the results list is not empty
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        
        # Check the structure of the first result
        if results:
            first_player = results[0]
            self.assertIn("name", first_player)
            self.assertIn("position", first_player)
            self.assertIn("team", first_player)
            self.assertIn("touchdowns", first_player)

if __name__ == '__main__':
    unittest.main()
