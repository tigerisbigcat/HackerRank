import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1

    for word in note:
        if word in d:
            d[word] -= 1
        else:
            d[word] = -1
    result = all([x >= 0 for x in d.values()])

    if result:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = ("7 4").split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = ("ive got a lovely bunch of coconuts").rstrip().split()

    note = ("ive got some coconuts").rstrip().split()

    checkMagazine(magazine, note)