from person import Person
import logging

logging.basicConfig(level=logging.INFO)


def sub(a, b):
    if b != 0:
        # (*) The following debug log was unreachable in original file because was written after return.
        # Then this log relocate for printing debug informations for developer.
        
        # (*) Moreover the DEBUG level replace with INFO because in this line, developer want to know
        # about sub function is working as expected.
        logging.info("a/b=" + str(a / b))
        return a / b    
    
    # (*) It's better to raise ValueError for returning error in terminal, but in this case
    # we ignore it because the file can't run after raise error, and p1&p2 Instances can not be instatiate
    # from Person class.
    logging.error("Divide by zero!")
    


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
