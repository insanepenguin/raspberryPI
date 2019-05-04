import random
x = 0;
while True:
    print(x)
    if x == 1:
        print("1")
    elif x == 2:
        print("2")
    else:
        print("Not")
    x = random.randint(1, 5)