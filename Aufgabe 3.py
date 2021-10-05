import random
nummer = random.randint(1,6)
counter=0
counteingabe=input("wie oft willst du würfeln?")
while counter<=int(counteingabe):
    nummer = random.randint(1,6)
    print("nummer ", nummer)
    counter+=1
