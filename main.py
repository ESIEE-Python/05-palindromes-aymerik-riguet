""" 
Voici la classe palindrome qui permet de verifier si une chaine de caractère est un palindrome.

"""
import unicodedata
#### Fonction secondaire


def ispalindrome(p):
    """

    Voici la fonction qui permet de réaliser sur la chaine de caractère donner en paramètre.

    """
    p = ''.join(c for c in unicodedata.normalize('NFD', p) if unicodedata.category(c) != 'Mn')
    for s in [" ",",","'","-","_","!","?",":"]:
        p = p.replace(s,"")
    p = p.lower()
    result1 = p[::-1]
    result2 = p
    return result1 == result2

#### Fonction principale


def main():
    """

    La fonction main() réalise des essaies afin de vérifier la fonction palindrome fonctionne.

    """

    print(ispalindrome("natan"))
    print(ispalindrome("poubelle"))
    print(ispalindrome("kayak"))
    print(ispalindrome("Câ,m imac"))

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
