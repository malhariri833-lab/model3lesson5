import random
playing=True
nummber=str(random.randint(0,9))
while playing:
    geuss=input("geuss the nummber: ")
    if nummber==geuss:
        print("u win")
        break