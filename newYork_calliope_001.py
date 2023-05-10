import unittest
from datetime import datetime

from carFactory import CarFactory

class ServiceableTest(unittest.TestCase):
    def test_NewYork_calliope_001(self):
        last_service_date = datetime(2018, 1, 1)
        current_date = datetime(2023, 5, 5)
        current_mileage = 40000
        last_service_mileage = 20000
        tires_sensors_numbers = [0.1, 0.3, 0.7, 0.8]
        calliope = CarFactory.create_calliope(current_date,
                                              last_service_date,
                                              current_mileage,
                                              last_service_mileage,
                                              tires_sensors_numbers)
        self.assertTrue(calliope.needs_service())

