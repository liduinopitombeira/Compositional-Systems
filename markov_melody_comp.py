# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:58:32 2019

@author: Liduino Pitombeira
"""

from music21 import *
import numpy as np



def MatrixTransition(A):
    
    #List with unique values of A and in ascending order 
    Aset = list(set(A))
    Aset.sort()
    print(Aset)

    #List of list filled with zeros (this will be filled by the iteractions)
    M = [[0]*len(Aset) for i in range(len(Aset))]

    #Gera a matriz de transição de proababilidades
    for i in range(len(A)-1):
        pos_linha = Aset.index(A[i])
        pos_coluna = Aset.index(A[i+1])
        M[pos_linha][pos_coluna]+=1
        
    #Normaliza a matriz
    for j in range(len(M)):
        total = sum(M[j])
        for k in range(len(M)):
            M[j][k] = (M[j][k])/total
    
    return(M)

#Extract the pitch parameter from a MIDI file
piece = converter.parse('melodiadiatonica.mxl').flat.getElementsByClass('Note').stripTies()
dados = [x.pitch.midi for x in piece]



print('Melodia original ',dados)

N = MatrixTransition(dados)
print('Matriz de transição = ', N)


#Sorteando através da matriz de transição

#Valor inicial
Bset = list(set(dados))
Bset.sort()
nota = np.random.choice(Bset, 1, True)
print('nota sorteada inicial = ',nota)

qte = 0
nova =[]

while qte < 30:
    nova.append(nota)
    nota = np.random.choice(Bset, 1, True, N[Bset.index(nota)])
    qte = qte + 1

#convertendo as arrays para inteiros
nova = [int(nova[i]) for i in range(len(nova))]

print('Nova melodia = ', nova)

durations = []

melodic_line = stream.Stream()

for i in range(len(nova)):
    nota = note.Note(nova[i])
    nota.quarterLength = 1
    melodic_line.append(nota)
    

melodic_line.write('mxl', 'novamelodiamarkov.mxl')