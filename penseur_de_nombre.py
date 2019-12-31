import random

# score = essai
essai = 0
rejouer = ("oui")
while rejouer != "non" or "n" :
    nombre_joueur = 0
    nombre = random.randint(1,99)
    # nombre = 46
    while nombre != nombre_joueur :
        essai += 1
        result = (nombre - nombre_joueur)
        nombre_joueur = int(input("entrer le nombre :"))
        if nombre == nombre_joueur :
            print("c'est gagner")
        elif nombre_joueur < nombre :
            if (nombre - nombre_joueur) <= 1 :
                print ("tu es brulant")
            elif (nombre - nombre_joueur) <= 5 :
                print ("tu chaufe")
            else :
                print("trop petit")
        elif nombre_joueur > nombre :
            if (nombre - nombre_joueur) <= 0 :
                print ("tu refroidis")
            else :
                print("trop grand")
    print ("Ton score est de {}".format(essai))
    # print (score)
    rejouer = input("veux tu rejouer ?")
