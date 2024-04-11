print("====================| ORDENADOR DE LISTAS |=======================================================")
lista=[]
for i in range(1,10):
    numero=float(input(f"DIGITE {i}ª NÚMERO: "))
    if numero==int(numero):
        lista.append(numero)
    else:
        print("Digite apenas números inteiros!")    
        continue
lista.sort()
print(lista)    