import unittest

from datetime import datetime
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
	def test_needs_service_false(self):
		last_service_date = datetime(2022, 1, 1)
		current_date = datetime(2023, 5, 5)
		battery = SpindlerBattery(last_service_date, current_date)
		#necessaryOrNot = "need" if battery.needs_service() else "don't need"
		#print("last_service_date is {}".format(str(last_service_date)))
		#print("current_date is {}".format(str(current_date)) +" and you " +necessaryOrNot+" to maintenance" )
		self.assertFalse(battery.needs_service())
	def test_needs_service_true(self):
		last_service_date = datetime(2020, 1, 1)
		current_date = datetime(2023, 5, 5)
		battery = SpindlerBattery(last_service_date, current_date)
		#necessaryOrNot = "need" if battery.needs_service() else "don't need"
		#print("last_service_date is {}".format(str(last_service_date)))
		#print("current_date is {}".format(str(current_date)) +" and you " +necessaryOrNot+" to maintenance" )
		self.assertTrue(battery.needs_service())
