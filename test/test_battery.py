import unittest
from datetime import date, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestBattery(unittest.TestCase):
    def setUp(self):
        # Set up any common data needed for the tests
        pass

    def test_nubbin_battery_needs_service(self):
        # Test the needs_service method of NubbinBattery
        nubbin_battery = NubbinBattery(last_service_date=date.today() - timedelta(days=365 * 2))
        self.assertTrue(nubbin_battery.needs_service())

    def test_spindler_battery_needs_service(self):
        # Test the needs_service method of SpindlerBattery
        spindler_battery = SpindlerBattery(last_service_date=date.today() - timedelta(days=365 * 2))
        self.assertTrue(spindler_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
