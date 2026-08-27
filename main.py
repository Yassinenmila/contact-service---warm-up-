import os

contacts = []

def sauvegarder_contacts():
    with open("contacts.txt", "w") as fichier:
        for contact in contacts:
            fichier.write(
                contact["nom"] + "|" +
                contact["telephone"] + "|" +
                contact["email"] + "\n"
            )

def ajouter_contact():

    nom = input("entrer le nom : ")
    telephone = input("entrer le numero de telephone : ")
    email = input("entrer l'email : ")

    contact= {
        "nom": nom,
        "telephone":telephone,
        "email":email
    }
        
    contacts.append(contact)

    sauvegarder_contacts()

    print("contact ajouter !!!!!!")


def afficher_contacts():
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        if not contacts:
            print("Aucun contact.")
            return

        for i, ligne in enumerate(contacts, start=1):
            nom, telephone, email = ligne.strip().split("|")

            print(f"{i}. {nom} | {telephone} | {email}")

    except FileNotFoundError:
        print("Aucun contact.")


def supprimer_contact():
    afficher_contacts()

    try:
        numero = int(input("Quel contact supprimer ? "))

        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        if numero < 1 or numero > len(contacts):
            print("Numéro invalide.")
            return

        contacts.pop(numero - 1)

        with open("contacts.txt", "w") as fichier:
            for contact in contacts:
                fichier.write(contact)

        print("Contact supprimé !")

    except ValueError:
        print("Veuillez entrer un numéro.")
    
    except FileNotFoundError:
        print("Aucun contact à supprimer.")


while True:
    input("\nAppuyez sur Entrée pour continuer...")
    os.system("clear")

    print("========== MENU ==========")
    print("1. Ajouter un contact ")
    print("2. Afficher les contacts ")
    print("3. Suprimer un contact")
    print("4. Quitter")

    choix = input("Votre choix : ")

    match choix:
        case "1":
            os.system("clear")
            ajouter_contact()
        case "2":
            os.system("clear")
            afficher_contacts()
        case "3":
            os.system("clear")
            supprimer_contact()
        case "4":
            break
        case _:
            print("choix invalide")
    
