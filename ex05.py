numpar=0
numimp=0
print(90*"=")
print("DIGITE 10 NÚMEROS PARA VERIFICAR SE SÃO PARES OU ÍMPARES")
print(90*"=")
for i in range(1,11):
    numero=int(input(f"Digite o {i}º número: "))
    if numero%2==0:
        numpar+=1
    else:
        numimp+=1
print(f"Você digitou {numpar} números pares e {numimp} números ímpares!")            