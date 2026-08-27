contacts = []


def ajouter_contact():
    pass


def afficher_contacts():
    pass


def supprimer_contact():
    pass


while True:
    print("========== MENU ==========")
    print("1. Ajouter un contact ")
    print("2. Afficher les contacts ")
    print("3. Suprimer un contact")
    print("4. Quitter")

    choix = input("Votre choix : ")

    match choix:
        case "1":
            print("ajouter un contact ")
        case "2":
            print("afficher un contact ")
        case "3":
            print("suprimer un contact ")
        case "4":
            break
        case _:
            print("choix invalide")
    
