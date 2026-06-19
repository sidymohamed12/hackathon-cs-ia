# ===================================
            # VARIABLE
# ===================================


# ===================================
            # CONDITION
# # ===================================
# nombre = int (input("entrer un nom : "))

# if nombre > 5:
#     print("ce nombre est superieur a 5")
# else :
#     print ("ce nombre est inferieur a 5")

# ===================================
            # BOUCLE
# ===================================

# x = int (input("entrer un nombre : "))

# while x > 5:
#     print("bonjour")




# programme addition_jusqua_n
# var 
# 	som, i, n, moy
# debut
# // contrôle de saisie
# 	faire
# 		afficher(“saisissez un nombre entier”)
# 		lire (n) 3
# 	tantque (n <= 0)

# 	som ← 0
# 	pour (i = 1, i <= n) faire  		1 – 2 – 3
# 		som ← som + i   	 0 + 1 – 1 + 2 – 2 + 3
# i ← i + 1		1+1 – 2+1 – 3+1
# finpour

# moy ← som / n

# afficher (‘la somme est :’, som)
# 	afficher (‘la moyenne est :’, moy)
# fin

# n = int (input("saisissez un nombre entier : "))

# while n < 0 or n == 0:
#     print ("ce nombre est negatif")
#     n = int (input("saisissez un nombre entier : "))

# som = 0
# for i in range(1, n+1):
#     som = som + i   # equivaut a som +=i

# moy = som/n


# print (f"la somme est : {som}")
# print (f"la moyenne est : {moy}")



# MIN, MAX, N, NOMBRE

N = int (input("saisissez un nombre entier : "))

while N <= 0:
    print ("ce nombre est negatif")
    N = int (input("saisissez un nombre entier : "))
    
liste=[]

for i in range(N):
    nombre = int (input("Entrer le nombre: "))
    liste.append(nombre)
    
    
print(liste)
print (f"Le nombre le plus grand est : {max(liste)}")
print (f"Le nombre le plus petit est : {min(liste)}")

    
    # if MAX is None or nombre > MAX :
    #     MAX = nombre
        
    # if  MIN is None or nombre < MIN :
    #     MIN = nombre
    






# ===================================
            # LISTE
# ===================================


# equipe = [
#   0 ->  "Barca",
#   1 ->  "Real",
#   2 ->  "Paris",
#   3 ->  "Manud",
#   4 ->  "Liv"
# ]

# equipes = [
#     "Barca",
#     "Real",
#     "Paris",
#     "Manud",
#     "Liv"
# ]
# print("\n----- ---------")
# print(equipes)

# # pour ajouter dans une liste :

# equipes.append("ManCity")
# print("\n----- ajout noirmal ---------")
# print(equipes)


# print("\n \n----- ajout avec liste ---------")
# equipes.append(["Arsenal", "Atletico"])
# print(equipes)


# # ===================================
#             # POP et remove
# # ===================================

# # pop prend l'indice de l'element a supprimer
# equipes.pop(1)
# print("\n \n-----Suppression dans la iste ---------")
# print(equipes)

# # remove prend la valeur de l'element a supprimer
# print("\n \n-----Suppression dans la iste ---------")
# equipes.remove("Manud")
# print(equipes)
