import datetime
current=datetime.datetime.now()
print("current time:",current.time())

import random

a=random.randint(0,1)
if (a==0):
    print("HEAD")
else:
    print("tail")
