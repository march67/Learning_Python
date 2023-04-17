nom = "david"

print(len(nom))  # len() permet de retourner le nombre de caractères
# affiche 5

print(nom.find("d"))  # String.find() permet de trouver la première position de la lettre en argument
# commence à 0
# pour "d" retourne et affiche 0, sensible à la casse

print(nom.capitalize())  # retourne "David", String.capitalize() permet de mettre la premiere lettre en majuscule
print(nom.upper())  # retourne "DAVID", String.upper() permet de mettre toutes les lettres en majuscule
print(nom.lower())  # retourne "david", opposé de upper()

print(nom.isdigit())  # objet.isdigit() retourne True ou False selon si l'objet est un entier

print(nom.isalpha())  # object.isalpha() retourne True ou False selon si la variable contient uniquement des lettres
# si un espace renvoie False

print(nom.replace("d", "o"))  # retourne "oavio", object.replace([arg1],[arg2])
# le premier argument est la lettre à remplacer, le  deuxième argument est son remplacement

print(nom*3) # retourne 3 fois la chaîne de caractère




