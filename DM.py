
alphaMin = 'abcdefghijklmnopqrstuvwxyz'

def decaler(letter, number):
    """
    Renvoie la lettre après le décalage d'une lettre de l'alphabet selon un nombre donné de positions
    :param letter: (str) La lettre à décaler
    :param number: (int) Le nombre de positions pour décaler la lettre
    :return: (str) La lettre après le décalage, ou la lettre initiale si ce n'est pas une lettre de l'alphabet
    """
    if letter in alphaMin:
        indiceDansAlpha = alphaMin.index(letter)
        nouveauIndice = (indiceDansAlpha + number) % len(alphaMin)
        return alphaMin[nouveauIndice]
    return letter


def crypter(name, number):
    """
    Renvoie un mot crypter en utilisant un décalage à chaque lettre
    :param name: (str) La chaîne de caractères à crypter
    :param number: (int) Le nombre de positions pour décaler chaque lettre du texte
    :return: (str) La chaîne cryptée après avoir appliqué le décalage à chaque lettre
    """
    newName = ""
    for caractere in name:
        newName += decaler(caractere, number)
    return newName


def nb_occurence(lettre, chaine):
    """
    La fonction 'nb_occurence' permet de compter le nombre d'occurrences d'une lettre donnée dans une chaîne de caractères.
    :param lettre: (str) La lettre qu'on veut compter le nombre d'occurrences
    :param chaine: (str) La chaîne de caractères
    :return: (int) Le nombre d'occurrences de la lettre
    """
    compteur = 0
    for char in chaine:
        if char == lettre:
            compteur += 1
    return compteur


def occurence_max(chaine):
    """
    Renvoie la lettre qui apparait le plus souvent dans la chaîne.
    :param chaine: (str) La chaîne de caractères
    :return: (str) La lettre d'occurrence maximale
    """
    lettre_max = ''
    occurence_max = 0
    for lettre in chaine:
        if lettre in alphaMin:
            nb_occur = nb_occurence(lettre, chaine)
            if nb_occur > occurence_max:
                occurence_max = nb_occur
                lettre_max = lettre
    return lettre_max


def decrypter(texte):
    """
    Décrypte un mot crypter par décalage de lettres.
    :param texte: (str) La chaîne de caractères cryptée
    :return: (str) La chaîne de caractères décryptée.
    """
    lettre_frequente = occurence_max(texte)
    decalage = alphaMin.index(lettre_frequente) - alphaMin.index('e')
    return crypter(texte, -decalage)
