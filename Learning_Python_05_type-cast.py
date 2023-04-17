# type cast / casting => convertis le type de donnée d'une valeur à un autre type de donnée

x = 1  # int
y = 2.5  # float
z = "3"  # str


# casting
print(float(x))  # retourne 1.0, x devient un float

print(int(y))  # retourne 2, y devient un entier

print(int(z)*3)  # print(z*3) retourne "333"
# print(int(z)*3) retourne 9

# exemple de casting utile
# print("X est : " + x)     # erreur de compilation car il y a une combinaison de string et d'un entier
# il faut dont appliquer le casting
print("X est : " + str(x))  # retourne "X est : 1"