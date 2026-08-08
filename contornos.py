#função que calcula o inverso de um contorno normalizado
def I (x):
    
    maior = max(x)
    novo = [maior - y for y in x]
    return novo
    
#função que calcula o retrógrado de um contorno normalizado
def R (x):
    
    return x[::-1]

#função que rotaciona o contorno normalizado em n posições
def ROT(x, n):
    return x[n:] + x[:n]


contorno_inicial = [int(x) for x in input('Entre com pontos de contorno normalizados separados por espaço: ').split()]
ciclo = int(input('Entre com o tamanho do ciclo ='))

print('Contorno original =',contorno_inicial)
print('=====================================')

inverso = I(contorno_inicial)
retrogrado = R(contorno_inicial)
rotacionado = ROT(contorno_inicial, 1)

print ('Inverso = ', inverso)
print ('Retrógrado = ',retrogrado)
print ('Rotacionado',rotacionado)

sequencia_base = [contorno_inicial, 
                  I(contorno_inicial), 
                  R(contorno_inicial)+I(contorno_inicial),
                  ROT(contorno_inicial, 1),
                  I(contorno_inicial)+contorno_inicial]

print('=====================================')
print('Sequencia =',sequencia_base*ciclo)


                  
                                                                                 
                                                                        

