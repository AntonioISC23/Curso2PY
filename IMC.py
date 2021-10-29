

masa=float(input("Ingresa tu masa en kilogramos: "))
altura=float(input("Ingresa tu altura en metros: "))

imc = masa/altura**2

print("El indice de masa corporal es: "+str(imc)) 

if imc > 25:
    print("tienes sobrepeso")
if imc< 19 :
    print("tienes bajo peso")