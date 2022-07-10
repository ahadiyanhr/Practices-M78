from time import ctime, strptime, mktime, time
from math import floor


class BirthDay():
    
    # Class attribute includes "name" and
    # "birthday" in 'Day Month Year Hour' format.
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    
    # Description of BirthDay class's Object
    def __str__(self):
        return f'{self.name} was born on {ctime(mktime(strptime(self.birthday, "%d %b %y %H")))}.' 

    
    # calAge method calculates the Object's age in year and hour:
    def calAge(self):
        ageInSec = time() - mktime(strptime(self.birthday, "%d %b %y %H"))
        ageInHour = floor(ageInSec / 3600)
        ageInYear = floor(ageInSec / 3600 / 24 / 365)
        return f"{self.name}'s live age is {ageInYear} years or {ageInHour} hours."
    
    # countdownBD method calculates the time until Object's next birthday:
    def countdownBD(self):
        # Find the next birthday in string:
        nextBDstring = self.birthday[:7] + str(int(ctime()[-2:])+1) + self.birthday[-3:]
        nextBDSec = mktime(strptime(nextBDstring, "%d %b %y %H"))
        remainSec = floor(nextBDSec - time())
        remainDay = floor(remainSec / 3600 / 24)
        remainHour = floor((remainSec - remainDay*3600*24) / 60 / 60)
        return f"Next Birthday countdown is {remainDay} days and {remainHour} hours."
    
hamid = BirthDay('Hamid', "11 Feb 90 04")
print(hamid)
print(hamid.calAge())
print(hamid.countdownBD())
print(ctime())


