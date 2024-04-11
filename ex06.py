intervalo=0
foraintervalo=0
print(90*"=")
print("INTERVALO [10,20]")
print(90*"=")
for i in range(1,11):
    numero=float(input(f"DIGITE O {i} NÚMERO: "))
    if numero>=10 and numero<=20:
        intervalo+=1
    else:
        foraintervalo+=1
print(f"{intervalo} números então no intervalo e {foraintervalo} números não estão no intervalo!")            