from datetime import datetime
from battery.battery import Battery


class SpindlerBattery(Battery):
	def __init__(self, last_service_date, current_date):
		current_date = datetime.now() if current_date == None else current_date
		print(current_date)
		self.last_service_date = last_service_date
		self.current_date = current_date
		print(current_date)

	def needs_service(self):
		diff_seconds = (self.current_date - self.last_service_date).total_seconds()
		diff_years = round(diff_seconds / 31536000, 2)
		return diff_years > 3