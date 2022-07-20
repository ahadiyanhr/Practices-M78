import logging


logging.basicConfig()
log_file_format = "%(asctime)s — %(name)-10s — %(levelname)-16s — %(funcName)s:%(lineno)d — %(message)s"

logging.basicConfig()
file_handler = logging.FileHandler('person.log', 'a')
log_format = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_file_format))


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
