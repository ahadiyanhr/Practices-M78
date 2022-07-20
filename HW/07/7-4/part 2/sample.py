from person import Person
import logging


log_file_format = "%(asctime)s — %(name)-10s — %(levelname)-16s — %(funcName)s:%(lineno)d — %(message)s"
log_console_format = "%(asctime)s — %(levelname)s — %(message)s"

logging.basicConfig()
logger = logging.getLogger('my_logger')
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('sample.log', 'a')
stream_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(log_console_format))
file_handler.setFormatter(logging.Formatter(log_file_format))

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def sub(a, b):
    if b != 0:
        logging.info("a/b=" + str(a / b))
        return a / b    
    logging.error("Divide by zero!")
    


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
