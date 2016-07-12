import sys
import random

total = 1
n = input("Enter the number of rows")
m = input("Enter the number of columns")
count = 0
mark = [[0 for x in range(m)] for y in range(n)]
def check():
    global count
    for x in range(m):
        for y in range(n):
            if mark[x][y] == 1:
                count+= 1
                if count == m:
                    print("Bingo you Won:row")
                    sys.exit(0)
                else:
                    count=0
        for x in range(m):
            for y in range(n):
                if mark[x][y] == 1:
                    count += 1
            if count == n:
                print("Bingo You Won:col")
                sys.exit(0)
            else:
                count=0


def locate():
    if total < m * n:
        y = (total - 1) // n
        x = (total - 1) % n
        if y % 2 == 1:
            x = (n - 1) - x
        print("The position is", y, x)

        mark[y][x] = 1
        for i in range(0, n):
            print mark[i]
        check()

while True:
    dice = random.randrange(1, 7)
    total = total + dice
    print("The number in the dice is", dice)
    if total < m * n:
        locate()
    elif total >= m * n:
        total = total - m * n
        locate()

