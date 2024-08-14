print("Bienvenido a la calculadora")
edad= int(input("Por favor ingrese su edad: "))
peso= int(input("por fa vor ingrese su peso: "))
estatura =int( input("ingrese su estatura en cm: "))
imc = peso/(estatura**2)
if imc < 18.5 :
    print("bajo Peso")
elif imc > 18.5 and imc < 24.9:
    print("normal")
else:
    print("sobrepeso")

