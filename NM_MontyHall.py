import numpy as np
from random import shuffle




#Funcion que retorna lista desordenada aleatoriamente con valores goat, goat y car
def sort_doors():
    lista=["goat","goat","car"]
    shuffle(lista)
    return lista

#Funcion que retorna numero aleatorio (0, 1 o 2) simulando primera eleccion de puerta
def choose_door():
    return np.random.choice(3, 1)[0]

#Funcion que retorna lista con una de las cabras descubiertas (Cambia un "goat" por "GOAT_MONTY" en la lista), y es una posicion distinta a la elegida inicialmente
def reveal_door(lista,choice):
    for i in range(np.size(lista)):
        if i != choice and lista[i] == "goat" :
            lista[i]="GOAT_MONTY"
            return lista

#Funcion que retorna eleccion final. Si change es False, no se cambia choice. Si es True, se cambia choice a otra posicion que no contenga "MONTY_GOAT"
def finish_game(lista, choice, change):
    if change == False:
        return lista[choice]
    else:
        for i in range(np.size(lista)):
            if i != choice and lista[i] != "GOAT_MONTY" :
                return lista[i]

#Simula 100 casos para choice = False
ganaFalse=0
for i in range(1000):
    choice=choose_door()
    lista=reveal_door(sort_doors(),choice)
    change=False
    if finish_game(lista, choice,change) == "car":
        ganaFalse+=1

#Imprime resultado para simulacion de 1000 casos con change = False
text1 ="La probabilidad de ganar el carro si no se cambia la puerta es "+ str(ganaFalse/1000.0)


ganaTrue=0
for i in range(1000):
    choice=choose_door()
    lista=reveal_door(sort_doors(),choice)
    change=True
    if finish_game(lista, choice,change) == "car":
        ganaTrue+=1

#Imprime resultado para simulacion de 1000 casos con change = True
text2 ="La probabilidad de ganar el carro si se cambia la puerta es "+ str(ganaTrue/1000.0)







print "Se realizan dos simulaciones de 1000 casos cada una. En la primera no se cambia de puerta tras revelarse la primera cabra, en la segunda si. Los resultados son:"

print text1
print text2












