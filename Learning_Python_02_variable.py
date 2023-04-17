# variable => un conteneur pour une valeur. Se comporte telle que la valeur
# qu'elle contient

# pas besoin de déclarer le type de la variable
# pas besoin de point virgule
nom = "David"
print("Bonjour " + nom) # combinaison d'une String brute et de l'utilsation d'une variable

print(type(nom)) # permet de vérifier le type de donnée et l'affiche à la console
# <class 'str'>

# convention de nommage de variable
# si la variable contient deux mots, séparer les deux mots par un underscore
nom_famille = "TA"

nom_entier = nom_famille + " " + nom
print(nom_entier)  # affiche la combinaison de deux variables

########
# type de donnée int (entier)
age = 21  # sans guillemet

age = age + 1  # équivalent de age += 1

print("J'ai : " + str(age) + " ans")  # affiche 22
# ne pas oublier de convertir l'entier dans la chaîne de caractère en String à
# l'aide de str()

print(type(age))  # <class 'int'>


####### float
taille = 169.5
print(taille)
print(type(taille)) # <class 'float'>

# print la variable taille avec un String
print("Ma taille est de : " + str(taille) + " cm")  # Ma taille est de : 169.5 cm
# ne pas oublier de convertir float en String à l'aide de str()


####### boolean
humain = True  # majuscule sur "False" / "True"
print(type(humain))  # <class 'bool'>
print("Es-tu un humain ? : " + str(humain))  # Es-tu un humain ? : True
# ne pas oublier de convertir float en String à l'aide de str()

