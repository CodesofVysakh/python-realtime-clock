import datetime
import time
def clock():
    while True:
        print(datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"), end="\r")
        time.sleep(1)

clock()