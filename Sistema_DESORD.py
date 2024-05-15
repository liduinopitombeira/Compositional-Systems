# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:25:25 2023

@author: Liduino Pitombeira
"""

import random as rd
from music21 import *



objeto, valor, ciclos = input('Entre com o objeto inicial, o valor e o tamanho do ciclo separados por espaço:').split()

if objeto=='1': 
    objeto1 = int(valor)
    objeto2=objeto3=objeto4=60
elif objeto=='2': 
    objeto2 = int(valor)
    objeto2=objeto3=objeto4=60
elif objeto=='3': 
    objeto3 = int(valor)
    objeto1=objeto2=objeto4=60
else: 
    objeto4 = int(valor)
    objeto1=objeto2=objeto3=60

chaves = ['12', '21', '13', '31', '14', '41', '23', '32', '24', '42', '43', '34']

ciclo = int(ciclos)
saida = []
usados = []
tabela = []
contador = 0

for x in range(ciclo):
    
    chave = rd.choice(chaves)
        
    if chave=='12': objeto2 = objeto1 + 1 
    elif chave=='21': objeto1 = objeto2 - 1 
    elif chave=='13': objeto3 = objeto1 + 5 
    elif chave=='31': objeto1 = objeto3 - 5
    elif chave=='14': objeto4 = objeto1 + 4
    elif chave=='41': objeto1 = objeto4 - 4
    elif chave=='23': objeto3 = objeto2 + 2
    elif chave=='32': objeto2 = objeto3 - 2
    elif chave=='24': objeto4 = objeto2 + 6
    elif chave=='42': objeto2 = objeto4 - 6
    elif chave=='34': objeto4 = objeto3 + 3
    elif chave=='43': objeto3 = objeto4 - 3
    saidaraw = set([objeto1, objeto2, objeto3, objeto4])
    saidareal = [x for x in saidaraw if x not in usados]
    usados = saidaraw
    saida.append(saidareal)
    
    tabela.append([contador, chave, objeto1, objeto2, objeto3, objeto4])
    contador += 1
    
saidaflat = sum(saida, [])
# saidaflat = [x + 60 for x in saidaflat]

print(saidaflat)

melodia = stream.Stream()

for i in range(len(saidaflat)):
    nota = note.Note(saidaflat[i])
    note.quarterLength = 1
    melodia.append(nota)
    
    
csv = "\n".join([",".join([str(y) for y in x]) for x in tabela])

with open('sistemadesord.csv', 'w') as f:
    f.write(csv)    
