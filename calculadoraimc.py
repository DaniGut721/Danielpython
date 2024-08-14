print("Bienvenido a la calculadora")
peso= int(input("por fa vor ingrese su peso: "))
estatura =int( input("ingrese su estatura en cm: "))
imc = peso/(estatura**2)
print("-----------------------")
if imc < 18.5 :
    print("bajo Peso")
elif imc > 18.5 and imc < 24.9:
    print("normal")
else:
    print("sobrepeso")
print("-----------------------")
