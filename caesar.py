def cesar_cipher(texte, decalage, mode):
    resultat = ""
    
    # Si on veut décrypter, on inverse simplement le décalage
    if mode == 'd':
        decalage = -decalage

    for i in range(len(texte)):
        char = texte[i]

        # Chiffrement des majuscules
        if char.isupper():
            resultat += chr((ord(char) + decalage - 65) % 26 + 65)
        # Chiffrement des minuscules
        elif char.islower():
            resultat += chr((ord(char) + decalage - 97) % 26 + 97)
        # Si ce n'est pas une lettre (espace, ponctuation), on ne touche à rien
        else:
            resultat += char

    return resultat

def main():
    print("--- Algorithme du Chiffre de César ---")
    choix = input("Voulez-vous (e)ncyrper ou (d)écrypter ? ").lower()
    
    if choix not in ['e', 'd']:
        print("Erreur : Choisissez 'e' ou 'd'")
        return

    message = input("Entrez votre message : ")
    try:
        shift = int(input("Entrez la valeur du décalage (nombre entier) : "))
    except ValueError:
        print("Erreur : Le décalage doit être un nombre.")
        return

    resultat = cesar_cipher(message, shift, choix)
    
    action = "crypté" if choix == 'e' else "décrypté"
    print(f"\nMessage {action} : {resultat}")

if __name__ == "__main__":
    main()