import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
	def test_needs_service_true(self):
		current_sensors_numbers = [0.1, 0.3, 0.9, 0.8]
		tires = CarriganTires(current_sensors_numbers)
		self.assertTrue(tires.needs_service())

	def test_needs_service_false(self):
		current_sensors_numbers = [0.1, 0.3, 0.7, 0.8]
		tires = CarriganTires(current_sensors_numbers)
		self.assertFalse(tires.needs_service())

