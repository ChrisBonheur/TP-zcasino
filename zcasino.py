#! /env/bin/python3
# coding: utf-8

import random as rdm
"""
    function to make play a roulete game
    with choice number and price from 
    player
"""
def play_game(number_choice, price):
    #Function to determine the categorie of number if its pai or impair
    def number_categorie(number):
        if number % 2 == 0:
            return "Un nombre pair" 
        else:
            return "Un nombre impair"
    
    random_number = rdm.randrange(50)
    print("==========>Le numero gagnant est le : {} Qui est {} ******".format(random_number, number_categorie(random_number)))
    
    if random_number == number_choice:
        winer_price = price * 3
        print("********************BRAVOOOOOOOOOOOOOO************************\n\
            Ainsi notre Champion vient de remporter {}$".format(winer_price))
        print("Il a misé sur le numéro {} Qui est un numéro gagnant !".format(number_choice,))
    elif number_categorie(number_choice) == number_categorie(random_number):
        winer_price = price / 2
        print("*************Pas mal vous avez gagnez {}$ avec {} *****************".format(winer_price, number_categorie(random_number)))
    else:
        print("********DESOLE VOUS AVEZ PERDU")

#########################################################################################################################
######################################### FUNCTION MAIN #################################################################
########################################################################################################################

def main():
    number_choice = input("Choisir un nombre entre 0 et 49 :")
    try:
        number_choice = int(number_choice)
        while number_choice > 49 or number_choice < 0:
            print('Attention Le nombre {} est incorect'.format(number_choice))
            number_choice = input("Choisir un nombre entre 0 et 49 : ")
            number_choice = int(number_choice)
            
        price = input("Choisir votre mise : ")
        price = int(price)
        while price < 2:
            print('Attention la somme misée est trop petite')
            price = input("Choisir votre mise : ")    
            price = int(price)

    except ValueError as e:
        print('Attention Erreur de valeur saisie : {}'.format(e))
    else:
        play_game(number_choice, price)

if __name__ == "__main__":
    main()