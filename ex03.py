print("--------------| TABUADA |----------------")
tab=int(input("Digite um valor inteiro de 1 a 10: "))

if tab<=10 and tab>0:
    print(f"TABUADA DO {tab}")
    for numtab in range(0,11):
        mul= tab*numtab
        print(f"{tab} X {numtab} = {mul}")
else:
    print("O Programa só aceita números de 1 a 10.")    