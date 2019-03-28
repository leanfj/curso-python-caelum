lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# imprimir maior elemento
print('Maior elemento da lista ', max(lista))

# imprimir menor elemento
print('Menor elemento da lista ', min(lista))

# imprimir os numeros pares
for pares in lista:
    if (pares % 2 == 0):
        print(pares)

# imprimir a ocorrencia do primeiro elemento da lista
primeiro_elemento = lista[0]
print('Ocorrência do primeiro elemento ', lista.count(primeiro_elemento))

# imprimir a media dos elementos
soma_elementos = 0
for elemento in lista:
    soma_elementos = soma_elementos + elemento
print('Media da soma dos elementos', soma_elementos // len(lista))

# imprimir a soma dos elementos negativos
soma_negativos = 0
for elemento in lista:
    if(elemento < 0):
        soma_negativos = soma_negativos + elemento
print('Soma dos numeros negativos', soma_negativos)
