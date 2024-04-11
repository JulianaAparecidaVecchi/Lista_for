
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

numero_mais_repetido = None
contagem_maxima = 0

for numero in lista:
    contagem = 0
    
    for outro_numero in lista:
        if outro_numero == numero:
            contagem += 1
    
    if contagem > contagem_maxima:
        numero_mais_repetido = numero
        contagem_maxima = contagem

print("O número que se repete mais vezes é:", numero_mais_repetido)
