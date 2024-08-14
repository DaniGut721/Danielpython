print("Bienvenido a la calculadora")
peso= int(input("por fa vor ingrese su peso: "))
estatura =int( input("ingrese su estatura en cm: "))
imc = peso/(estatura**2)
print("-----------------------")
if imc < 18.5 :
    print( "su condicion: bajo Peso")
elif imc > 18.5 and imc < 24.9:
    print(" su condicion: normal")
else:
    print("sobrepeso")
print("-----------------------")
print("esto fue hecho en github")
