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
        "nom"= nom,
        "telephone"=telephone,
        "email"=email
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
            ajouter_contact()
        case "2":
            afficher_contacts()
        case "3":
            supprimer_contact()
        case "4":
            break
        case _:
            print("choix invalide")
    
