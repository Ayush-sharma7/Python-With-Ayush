# tower of hanoi
import math


def moves(n):
    return math.pow(2, n) - 1


a = int(input("enter number of discs: "))
print("moves: ", moves(a))
