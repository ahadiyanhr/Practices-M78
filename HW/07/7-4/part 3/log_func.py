log_levels = [
    'DEBUG',
    'INFO',
    'WARNING',
    'ERROR',
    'FATAL',
    'CRITICAL'
]

def log_func(file: str, level: str):
    
    log_num = 0
    with open(file, 'r') as f:
        line_list = f.readlines()

    for line in line_list:
        for levels in log_levels[log_levels.index(level.upper()):]:
            if levels.upper() in line:
                log_num += 1
            
    return log_num

print(log_func('person.log', 'warning'))