import unittest

from main import whole_mission_fuel


class TestFuelCalculator(unittest.TestCase):

    def test_apollo11(self):
        self.assertEqual(whole_mission_fuel(28801, [(9.807, 1.62), (1.62, 9.807)]), 51898)

    def test_mission_on_mars(self):
        self.assertEqual(whole_mission_fuel(14606, [(9.807, 3.711), (3.711, 9.807)]), 33388)

    def test_passenger_ship(self):
        self.assertEqual(whole_mission_fuel(75432, [(9.807, 1.62), (1.62, 3.711), (3.711, 9.807)]), 212161)


if __name__ == '__main__':
    unittest.main()
