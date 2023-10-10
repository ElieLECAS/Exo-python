blague = "Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?"
autre = "Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste "


print(blague)
# reponse = input("Votre réponse : ")

while True:
            
    reponse = input("Votre réponse : ")


    if reponse == "repete":
        print(blague)
        # reponse = input("Votre réponse : ")

    elif reponse == "tu es lourd":
        print("ahah")
        break
    
    else:
        print(autre)
        # reponse = input("Votre réponse : ")