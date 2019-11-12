#for timing
import time
#to hold the number of each dice roll
from collections import Counter
yahtzeeUpperList = [[2, 3, 5, 5, 6],[1, 1, 1, 1, 3],[1, 1, 1, 3, 3],[1, 2, 3, 4, 5],[6, 6, 6, 6, 6]]
yahtzeeUpperListLong = [1654, 1654, 50995, 30864, 1654, 50995, 22747, 1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654, 30864, 4868, 30864]

with open("PythonAttempts/2019-11-11/yahtzee-upper-1.txt", "r") as f:
    data = f.read().splitlines()

#yahtzee_upper
#takes a roll of dice and computes the max product
#from that rolls Counter
def yahtzee_upper(roll):
    counts = Counter(roll)
    maxScore = 0
    for x, y in counts.items():
        product = int(x) * y
        if product > maxScore:
            maxScore = product
    return maxScore

start = time.time()

for roll in yahtzeeUpperList:
    print(yahtzee_upper(roll))

end = time.time()
print('Easy Completed in ',end - start,' seconds.')
start = time.time()

print(yahtzee_upper(yahtzeeUpperListLong))

end = time.time()
print('yahtzeeUpperListLong Completed in ',end - start,' seconds.')
start = time.time()

print(yahtzee_upper(data))

end = time.time()
print('Optional Completed in ',end - start,' seconds.')