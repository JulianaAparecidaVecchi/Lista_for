print(90*"-")
print(" -------| SOMA PAR |------- ")
print(90*"=")
somapar=0
for i in range(1,101):
    if i%2==0:
        somapar+=i
print(f"A soma dos 50 primeiros números pares é {somapar}")        
print(90*"-")