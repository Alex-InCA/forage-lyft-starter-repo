from typing import List
from tires.tires import Tires


class octoprimeTires(Tires):
    def __init__(self, current_sensors_numbers: List[float]):
        self.current_sensors_numbers = current_sensors_numbers

    def needs_service(self):
        for c in self.current_sensors_numbers:
            if c >= 3.0:
                return True
        return False