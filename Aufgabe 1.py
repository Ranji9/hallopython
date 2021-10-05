print ("Hallo Python") 
import random
nummer = random.randint (1,6)
print(nummer)
import random
nummer = random.randint (1,6)
counter = 0
for counter in range(0,5):
    nummer = random.randint (1,6)
    print("nummer: ", nummer)
    counter= counter+1
    print("anzahl counter benutzt:",counter)

