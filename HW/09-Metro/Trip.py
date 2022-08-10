import logging
from User import User
from other_func import get_owner

# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'metro.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

class Trip:
    
    _trip_records = {}
    
    def __init__(self, origin: str, destination: str, fare: int):
        self.origin = origin
        self.destination = destination
        self.fare = fare
    
    @classmethod    
    def record_trip(cls, origin, destination, fare, auth_code):
        trip_number = len(Trip._trip_records)+1
        Trip._trip_records[trip_number] = (auth_code, Trip(origin, destination, fare))
        logging.log(logging.INFO, f"A Trip No.{trip_number} takes by user with Authentication Code of {auth_code}")
        return True
