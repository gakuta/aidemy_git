import random

with open("./hyakunin.txt", encoding="utf-8") as f:
    wakes = [s.strip() for s in f.readlines()]

print(wakas[random.randrange(len(wakes))])
