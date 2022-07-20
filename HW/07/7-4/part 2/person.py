import logging

log_file_format = logging.Formatter("%(asctime)s — %(name)-10s — %(levelname)-16s — %(message)s")

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger('root')
file_handler = logging.FileHandler('person.log', 'a')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_file_format)
logger.addHandler(file_handler)

class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
            logging.info("Person created! {} {}".format(self.name, self.family))
        else:
            logging.error("Invalid age!")
            self._age = 0
