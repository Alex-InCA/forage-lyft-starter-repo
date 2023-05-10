import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
	def test_needs_service_true(self):
		current_sensors_numbers = [0.1, 3, 0.9, 0.8]
		tires = OctoprimeTires(current_sensors_numbers)
		self.assertTrue(tires.needs_service())
	def test_needs_service_false(self):
		current_sensors_numbers = [0.1, 2.9, 0.9, 0.8]
		tires = OctoprimeTires(current_sensors_numbers)
		self.assertFalse(tires.needs_service())
