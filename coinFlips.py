import random
print("I wil flip a coin 1000 times. Guess how many times it will come up heads. (Press 'enter' to begin)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print("At 900 flips, there have been {} heads\n".format(str(heads)))
    if flips == 100:
        print("At 100 flips, there have been {} heads\n".format(str(heads)))
    if flips == 500:
        print("After 500 flips(halfway) there have been {} heads\n".format(str(heads)))

print("Out of 1000 coin tosses, heads came up {} times\n".format(str(heads)))
