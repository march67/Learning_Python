# demande la saisie d'un utilisateur
input("Quelle est ton prénom ? ")  # input() permet de demander la saisie d'un utilisateur
# l'argument dans input est un String qui permet d'afficher le text (question) à l'utilisateur

# pour utiliser la valeur renvoyée il faut l'affecter à une variable

nom = input("Quelle est ton prénom ? ")
age = int(input("Quelle est ton âge ? "))  # il faut cast car la valeur saisie sera toujours
# un String, ici on veut appliquer une opération +1 à cette valeur, il faut donc le convertir en int
age += 1

taille = float(input("Quelle est ta taille en cm ? "))

print("Mon nom est " + nom + ", mon âge est de " + str(age) + " an" + " ,je mesure " + str(taille) + "cm")
# affiche la valeur saisie par l'utilisateur
# age est maintenant un int, il faut cast en String avec str()
