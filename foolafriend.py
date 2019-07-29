import webbrowser
import time
import random
while True:
    s=random.choice(['google.com','youtube.com','facebook.com','danielsam17l31a0534'])
    visit="http://{}".format(s)
    webbrowser.open(visit)
    sec=random.randrange(1,3)
    time.sleep(sec)
