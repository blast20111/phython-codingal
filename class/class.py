class veichle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(veichle):
    pass
School_bus=bus("school volvo",240,18)
print("veichle name",School_bus.name,"veichle speed",School_bus.max_speed,"mileage",School_bus.mileage)