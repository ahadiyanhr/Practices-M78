import logging

# (*) The overall logging level is more than the body's log levels.
# it is better to set the overall logging level to INFO to force code shows the all logs:
logging.basicConfig(level=logging.INFO)


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
            
            # This log relocate from __init__ to below line because it must run
            # when instance created without any problem.
            logging.info("Person created! {} {}".format(self.name, self.family))
        else:
            # (*) The logging.critical is more than needed for this kind of errors.
            # because the code was unable to perform some function but it does not shut-down by that!!
            # this log replace with logging.error:
            logging.error("Invalid age!")
            
            # (*) {self._age = 0} must be in the scope of else statement as logging.critical
            # in order to set negative ages to a non-negative value:
            self._age = 0
