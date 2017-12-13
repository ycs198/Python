#!/usr/bin/python
from datetime import datetime
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
right = datetime.today().minute
if right in odds:
    print ("This minute seems a little odd.")
else:
    print ("Not an odd minute.")