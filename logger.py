


from datetime import datetime as dt
from time import time

def number_logger(text):
    time = dt.now().strftime('%c')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write('{};HR Department;{}\n'
                   .format(time, text))