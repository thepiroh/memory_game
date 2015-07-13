__author__ = 'iAntoine'

import random
import os
import time

f = open("verbesEn.txt", "r")
num_lines = sum(1 for line in open('verbesEn.txt')) # number of lines of txt file
dico = [i for i in xrange(num_lines)]
reponse = [i for i in range(num_lines)]
score = 0
mode = 0
visited = []

for i in xrange(num_lines):
    dico[i] = f.readline().replace('\n', '')
f.close()

while True:
    try:
        nombreMots = int(raw_input("Combien de mots:"))
        secondes = int(raw_input("Combien de secondes:"))
        break
    except ValueError:
        print("Erreur: Veuillez choisir un nombre entier:")
if (nombreMots >= 5) and (secondes <= 20):
    print("Vous avez choisi le mode: Moyen")
    mode = 5
elif (nombreMots >= 10) and (secondes < 15):
    print("Vous avez choisi le mode: Difficile")
    mode = 10
else:
    print("Vous avez choisi le mode: Facile")
    mode = 1
listeRandom = random.sample(range(1, num_lines), nombreMots)

for i in range(nombreMots):
    reponse[i]= dico[listeRandom[i]]
    print(reponse[i])

time.sleep(secondes)
os.system('clear')

print("Alors c'etait quoi?")

debut = time.time()
for i in range(0, nombreMots):

    userReponse = raw_input()
    if (userReponse in reponse):
        if userReponse in visited:
            print("NO, tu as deja dit ca...")
        else:
            print("YES")
            score+=1
        visited.append(userReponse)
    else:
        print("NO")
fin = time.time()

print("Reponses justes: {} / {}".format(score, nombreMots))
print("Score: {}".format(score*mode))
print("Vous avez fini en {} secondes".format(int(fin-debut)))
print("les reponses etaient: ")
for i in range(nombreMots):
    print(reponse[i])
