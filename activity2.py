import random
while True:
    useraction=input("inter a choose rock papier or sesior: ")
    possibleaction=["rock","sesior","papier"]
    compeuteraction=random.choice(possibleaction)


    if useraction==compeuteraction:
        print("both players selcted the same ",useraction)
    elif useraction=="rock":
        if compeuteraction=="sesior":
            print("u won ")
        else:
            print("compeuter won")

    elif useraction=="papier":
            if compeuteraction=="sesior":
                print("compeuter wins ")
            else:
                print("u win ")
    elif useraction=="sesior":
            if compeuteraction=="rock":
                print("compeuter wins")
            else:
                print("u win")
    playagin=input("do u want to play again Y or N") 
    if playagin!="Y":
         break
    

         
