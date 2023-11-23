#11.1+11.2
import unittest
from city_functions import format_city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        formatted_result = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_result, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_result = format_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_result, 'Santiago, Chile – population 5000000')

if __name__ == '__main__':
    unittest.main()
