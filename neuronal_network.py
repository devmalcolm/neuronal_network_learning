# coding: utf-8
# Le neuronal network actuel que j'utilise est un 2 inputs (Input_A & Input_B ) donc les 2 entrées.
# Ensuite les 2 entrées sont redirigés par les 3 synapses qui sont reliées aux 3 "hidden Layer"
# Qui ensuite sont redirigés par les 3 synapses --> output Layer
# --
# Pour le tableau, j'ai décidé de prendre pour exemple un tableau avec 10 valeurs & 3 colonnes
# Pour le context il y aura un système de voiture & camion. [ 0 pour la voiture & 1 pour le camion ] 
# Ainsi que leur dimensions donc longeur du vehicule et largeur

# Importations des modules
import numpy as np 
import matplotlib.pyplot as plt
import mplcyberpunk
import time as t
import os 

# Input_A = Longueur & Largeur (valeur dans le tableau)
# Input_B = 0 -> voiture | 1 -> camion

# Définir les entrées avec les valeurs du tableau
input_dimension = np.array(([3.5,1.5], [9.3,2.3], [5.5,2.7], [7.3,2.5], [2.3,1.7], [6.9,2.9], [2.7,1.6], [3.9,1.8], [8.3,3], [6.4,2.2]), dtype=float)
# Dans l'input B il n'y a que 9 valeurs car il nous faut trouver la 10ème valeur (celle manquante)
input_type = np.array(([0], [1], [1], [1], [0], [1], [0], [0], [1]), dtype=float)

 
# On divise par le plus grand chiffre pour nous permettre d'obtenir des valeurs entre 0 & 1
# Axis est égal a l'axe dont on veut calculer nos valeurs
input_a_divided = input_dimension/np.amax(input_dimension, axis=0)

# On split les valeurs donc on recupère seulement les valeurs avec un résulat donc les 9 première
split_value = np.split(input_a_divided,[9])[0]
split_prediction = np.split(input_a_divided,[9])[1]

# Création d'une classe pour le reseaux neuronal
class neuronal_network:
    def __init__(self):
        # Les valeurs ci-dessous sont celles retrouvé sur l'image qui illustre ce code.
        self.inputNeuronal = 2
        self.hiddenNeuronal = 3
        self.outputNeuronal = 1

        self.weight1 = np.random.randn(self.inputNeuronal, self.hiddenNeuronal)
        self.weight2 = np.random.randn(self.hiddenNeuronal, self.outputNeuronal)

    def feedforward(self, split_value):
        # La variable self.multi multiplie la valeur d'entrer donc qui est maintenant split_value, et on la multiplie par self.weight1
        # Et donc ensuite avec self.sigmoid_cal on effectue la fonction sigmoid dessus (j'ai du mal avec)
        self.multi_1 = np.dot(split_value, self.weight1)
        self.sigmoid_cal_1 = self.sigmoid_equation(self.multi_1)
        self.multi_2 = np.dot(self.sigmoid_cal_1, self.weight2)
        output_sigmoid = self.sigmoid_equation(self.multi_2)
        return output_sigmoid


    # On créer une fonction pour écrire le calcule de la fonction sigmoid afin de l'appliquer au dessus
    def sigmoid_equation(self, S):
        return 1/(1+np.exp(-S))

# Output de notre calcul matriciel
output_result = neuronal_network().feedforward(split_value)


# J'ai crée ici un graphique pour mieux se visualiser le tableau & comparer
plt.style.use("cyberpunk")
plt.plot(split_value, marker='o', label='Bleu = Largeur & Rose = Longueur')
plt.legend(loc='lower left')
mplcyberpunk.add_glow_effects()


def question_choice():
    while True:
        print("""
1. Afficher les données de l'IA
2. Afficher le graphique
3. Afficher les deux

        """)
        input_question = input(str("Veuillez choisir: "))
        if input_question == '1':
            print("La sortie prédite par l'IA: ", str(output_result))
            print("La sortie réel: ", str(input_type))
            break
        elif input_question == '2':
            print(plt.show())
            break
        elif input_question == '3':
            print(output_result, plt.show())
        else:
            os.system("clear")
            print('[ERREUR] Veuillez choisir un élément ci-dessus !')
            t.sleep(2)
            os.system("clear")


if __name__ == "__main__":
    question_choice()

# A ce stade la l'AI fait juste crée un tableau avec des valeurs, leur soumettre la fonction d'activation qui est la fonction sigmoid, ainsi que input_a_divided qui va garder toute nos valeurs 
# entre 0 & 1 donc actuellement on a des valeurs qui sont sortie grâce au calcul matriciel dans la class neuronal_network mais le soucis est que les valeurs des weights donc des poids/synaps
# sont actuellement générer aléatoirement ce qui fait qu'il faut utilisé la "rétropropagation" afin d'obtenir des résultats proche de la réalité, malheureusement étant donné que j'apprend 
# en auto didacte sur ce sujet là il est compliqué de comprendre plein chose tel que certaine fonction mathématique ou autre.


