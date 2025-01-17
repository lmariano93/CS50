import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

r = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess != 0:
            if guess < r:
                print("Too small!")
            elif guess > r:
                print("Too large!")
            else:
                print("Just Right!")
                break
    except:
        pass
