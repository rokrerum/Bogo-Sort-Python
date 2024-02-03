import time
import random

def arm(func):
    def wrapper():
        before = time.time()
        func()
        print(str(round(time.time() - before, 2)) + " sec")
    return wrapper

array = []
for i in range(9):
    array.append(random.randint(1, 100))

def check():
    global a
    a = 0
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            a = a + 1

def bogo_sort():
    for i in range(len(array)):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        tmp = array[x]
        array[x] = array[y]
        array[y] = tmp
    print(array)

@arm
def bogo():
    moves = 0
    check()
    while True:
        bogo_sort()
        check()
        moves = moves + 1
        if a == 0:
            print(f"Sorting took {moves} moves")
            break

bogo()
#created by: rokrerum