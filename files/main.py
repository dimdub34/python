#! /usr/bin/env python3

import pickle


def get_dict():
    try:
        with open("passwords.pck", "rb") as f:
            the_dict = pickle.load(f)
    except IOError:
        with open("passwords.pck", "wb") as f:
            pickle.dump({}, f)
        return get_dict()
    return the_dict


def save_dict(the_dict):
    with open("passwords.pck", "wb") as f:
        pickle.dump(the_dict, f)


def get_passwd(le_mot, nb_lettres=4):
    the_dict = get_dict()
    if le_mot in the_dict.keys():
        print("Le mot de passe existe déjà")
        return the_dict[le_mot]
    else:
        try:
            mot = le_mot[:nb_lettres]
            count_lettres = [le_mot.count(l) for l in mot]
            le_password = f"!{mot.upper()}_{''.join(map(str, count_lettres))}=$"
        except (TypeError, AttributeError):
            return "Il faut passer une chaîne de caractère en argument"
        else:
            print("Enregistrement du mot de passe")
            the_dict[le_mot] = le_password
            save_dict(the_dict)
            return le_password


if __name__ == "__main__":
    print("Bonjour")
    mot_donne = input("Veuillez saisir le mot pour lequel vous souhaitez un mot de passe : ")
    print(f"Le mot de passe correspondant au mot {mot_donne} est {get_passwd(mot_donne)}")
    print("Au revoir")
