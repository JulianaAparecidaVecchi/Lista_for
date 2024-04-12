somaida=0
totalida=0
idade=1
print(90*"=")
print("| MÉDIA IDADES |")
print(90*"=")
print("Quando quiser encerrar o programa e exibir a média digite '0'")
while True:
    
    if idade==0:
        break

    idade=float(input("DIGITE UMA IDADE: "))
    somaida+=idade
    totalida+=1
    media=somaida/totalida
print(f"A média das idades digitadas é {media:.2f}")    