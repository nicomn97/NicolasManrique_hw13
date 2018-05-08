import numpy as np
from random import shuffle




#Funcion que retorna lista desordenada aleatoriamente con valores goat, goat y car
def sort_doors():
    lista=["goat","goat","car"]
    shuffle(lista)
    return lista

#Funcion que retorna numero aleatorio (0, 1 o 2)
def choose_door():
    return np.random.choice(3, 1)[0]

#Funcion que retorna lista con una de las cabras descubiertas ("Cambia goat por GOAT_MONTY"), y es una posicion distinta a la elegida
def reveal_door(lista,choice):
    for i in range(np.size(lista)):
        if i != choice and lista[i] == "goat" :
            lista[i]="GOAT_MONTY"
            return lista

#Funcion que retorna numero aleatorio (0, 1 o 2)
def finish_game(lista, choice, change):
    if change == False:
        return lista[choice]
    else:
        for i in range(np.size(lista)):
            if i != choice and lista[i] != "GOAT_MONTY" :
                return lista[i]


ganaFalse=0
for i in range(100):
    choice=choose_door()
    lista=reveal_door(sort_doors(),choice)
    change=False
    if finish_game(lista, choice,change) == "car":
        ganaFalse+=1

print ganaFalse

ganaTrue=0
for i in range(100):
    choice=choose_door()
    lista=reveal_door(sort_doors(),choice)
    change=True
    if finish_game(lista, choice,change) == "car":
        ganaTrue+=1

print ganaTrue














