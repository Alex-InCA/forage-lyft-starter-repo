from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        #print("self.current_mileage - self.last_service_mileage is {}".format(str(self.current_mileage - self.last_service_mileage)))
        return self.current_mileage - self.last_service_mileage > 30000
