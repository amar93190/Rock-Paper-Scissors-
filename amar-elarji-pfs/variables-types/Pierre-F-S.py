import random, time

score_humain = 0
score_robot = 0

user_play = input("Souhaitez-vous initier une session de pierre-papier-ciseaux ? [o/n] ")
ai_option_list = ['r', 'p', 's', 'Pierre', 'Papier', 'Ciseaux']

while user_play == 'o' or user_play == 'oui':
    user_pick = input("Veuillez choisir 'r' pour pierre, 'p' pour papier, ou 's' pour ciseaux : ")

    random.seed()
    ai_choose = random.randint(0, 2)
    ai_pick = ai_option_list[ai_choose]

    def replaceStr(choose):
        if choose == 0:
            print("Le robot choisit", ai_option_list[3])
        elif choose == 1:
            print("Le robot choisit", ai_option_list[4])
        elif choose == 2:
            print("Le robot choisit", ai_option_list[5])

    if user_pick == 'r' and ai_pick == 's' or user_pick == 'p' and ai_pick == 'r' or user_pick == 's' and ai_pick == 'p':
        replaceStr(ai_choose)
        time.sleep(1)
        print("Vous avez gagné !")
        score_humain += 1
        time.sleep(1)
    elif user_pick == ai_pick:
        replaceStr(ai_choose)
        time.sleep(1)
        print("Égalité. Veuillez procéder à une nouvelle tentative.")
        time.sleep(1)
    else:
        replaceStr(ai_choose)
        time.sleep(1)
        print("Le robot a gagné !")
        score_robot += 1
        time.sleep(1)

    print("Score actuel - vous :", score_humain, "| adversaire :", score_robot)
    user_play = input("Souhaitez-vous  une nouvelle partie ? [o/n] ")

if user_play != 'oui' or user_play != 'o':
    print("Fin de la session de jeu. Merci de votre participation.")
    print("Score vous :", score_humain, "| adversaire :", score_robot)
    quit()
