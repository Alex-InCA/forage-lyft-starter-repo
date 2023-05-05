import unittest

from datetime import datetime
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
	def test_needs_service_false(self):
		last_service_date = datetime(2022, 1, 1)
		current_date = datetime(2023, 5, 5)
		battery = NubbinBattery(last_service_date, current_date)
		self.assertFalse(battery.needs_service())
	def test_needs_service_true(self):
		last_service_date = datetime(2019, 1, 1)
		current_date = datetime(2023, 5, 5)
		battery = NubbinBattery(last_service_date, current_date)
		self.assertTrue(battery.needs_service())
