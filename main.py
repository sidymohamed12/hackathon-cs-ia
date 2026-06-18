
# gestion de stock
#  fonctionnalité : 
    # - ajouter produit   ==> khalil
    # - lister produit    ==> Omar 
    # - modifier produit  ==> Sidy
    # - supprimer produit
    # - ajouter un client => khalil
    # - supprimer un cient => yhh ammannnnnnnnn
    # - supprimer un cient => souleymane "hello world"
    #Ibrahima Sarr    


# 2 types d'approches
# - 1ere approche : chacun cree sa branche et y travaille
    #  - dev/omar
    #  - dev/khalil
    #  - dev/sidy



# - 2e approche : une branche par fonctionnalite
    #  - feat/lister-produit  => Omar
    #  - feat/add-product  => khalil
    #  - feat/update-product => Sidy
    

# cree une branche develop : branche en commun
# chacun va merge son travail dans develop   
    
# feat -> feature ? fonnctionnalité


# les commandes

    # pour creer une branche et l'envoyer dans github
        # git checkout -b le-nom-de-la-branche
        # git push -u origin le-nom-de-la-branche

    # pour ajouter les modif sur github
        # 1- git add .
        # 2- git commit -m "ajout de quelque chose"
        # 3- git push
    
    # pour merge :
        # d'abord se pointer sur cette branche : 
            #  git checkout le-nom-de-la-branche
        # git merge le-nom-de-la-branche-a-merge
        # git push
        
    # pour recuperer les dernieres modifs d'une branche :
        # d'abord se pointer sur cette branche : 
            #  git checkout le-nom-de-la-branche
        # ensuite pour recuperer les modifs :
            #  git pull
            
            
# if 1 > 2:
#     print("yhhhhhh")
# else:
#     print("ooohhhhh")
#     print("eehhhhhh")
    
# print("je suis liiibbrrreeee")


fruits = [
            "pomme", 
            "banana", 
            "fraise",
            [
                "ok",
                "yh"
            ]
          ]

print(fruits[3][0])