import string
import logging
import random
import argparse

# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'pass_log.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

## characters to generate password from
char_list = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def pass_generator(characters: list = char_list, length: int = 6,\
    numbers: int = 1, start: str = '', output: str = 'my_pass.txt'):
    
    for _ in range(numbers):
        
        ## shuffling the characters
        random.shuffle(characters)
        password = random.sample(random.shuffle(characters), length-len(start))
        password = start+"".join(password)
        

        with open(output, 'w+') as file:
            file.write(password)

    s_str = ''
    if numbers != 1:
        s_str = 's'
    logging.log(logging.INFO, f"{numbers} password{s_str} is generated and saved into {output}.")


parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", dest='chars', type=int, help="the necessary words that must be in password")
parser.add_argument("-o", "--output", dest='filename', default='my_pass.txt', help="the output filename")
parser.add_argument("-l", "--length", dest='pass_length', nargs=2, default=['4', '8'], help="length of characters")
parser.add_argument("type", type=int, help="password generator type")
args = parser.parse_args()



print('chars =', args.chars)
print('filename =', args.filename)
print('pass_length =', args.pass_length)
print('type =', args.type)


# set txt extension for filename if does not exist:
if '.' not in args.filename[-5:]:
    filename = args.filename+'.txt'