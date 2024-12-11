import random

def poser_questions(table):
    """Pose les questions pour une table donnée."""
    nombres = list(range(0, 11))  # Liste des nombres à utiliser (sans remise)
    random.shuffle(nombres)      # Mélange pour plus d'aléatoire

    while nombres:  # Tant qu'il reste des nombres à interroger
        nombre = nombres.pop()  # Sélectionne et retire un nombre
        print(f"Combien font {table} x {nombre} ?")
        
        # Validation de la réponse utilisateur
        while True:
            try:
                reponse = int(input("Votre réponse : "))
                break
            except ValueError:
                print("S'il vous plaît, entrez un nombre valide.")

        # Vérification de la réponse
        if reponse == table * nombre:
            print("Bonne réponse !")
        else:
            print("Essaie encore, ce n'est pas le bon résultat.")
            nombres.append(nombre)  # Remet le nombre pour réessayer

    print(f"Vous avez terminé la table {table} !")

def programme_principal():
    """Boucle principale pour gérer le programme."""
    print("Bienvenue au programme de révision des tables de multiplication !")
    while True:
        # Demande à l'utilisateur la table à réviser
        while True:
            try:
                table = int(input("Quelle table voulez-vous réviser ? "))
                if table < 0:
                    print("La table doit être un entier positif.")
                else:
                    break
            except ValueError:
                print("S'il vous plaît, entrez un nombre valide.")
        
        # Lancer les questions pour la table choisie
        poser_questions(table)

        # Demander à l'utilisateur s'il veut continuer ou quitter
        while True:
            continuer = input("Voulez-vous réviser une autre table ? (o/n) : ").lower()
            if continuer in ("o", "n"):
                break
            else:
                print("Veuillez répondre par 'o' pour oui ou 'n' pour non.")
        
        if continuer == "n":
            print("Au revoir et à bientôt !")
            break

# Lancer le programme principal si le script est exécuté directement
if __name__ == "__main__":
    programme_principal()
