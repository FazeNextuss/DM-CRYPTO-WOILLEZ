alphaMin = 'abcdefghijklmnopqrstuvwxyz'

def decaler(letter, number):
    if letter in alphaMin:
        indiceDansAlpha = alphaMin.index(letter)
        nouveauIndice = (indiceDansAlpha + number) % len(alphaMin)
        return alphaMin[nouveauIndice]
    return letter

def crypter(name, number):
    newName = ""
    for caractere in name:
        newName += decaler(caractere, number)
    return newName

def nb_occurence(lettre, chaine):
    compteur = 0
    for char in chaine:
        if char == lettre:
            compteur += 1
    return compteur

def occurence_max(chaine):
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
    lettre_frequente = occurence_max(texte)
    decalage = alphaMin.index(lettre_frequente) - alphaMin.index('e')
    return crypter(texte, -decalage)
