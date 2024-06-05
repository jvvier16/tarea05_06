def suma_2_numeros():


    num1 = float(input("ingrese primer número:"))
    num2 = float(input("ingrese el segundo número:"))
    total = num1+num2
    print("el total de la suma es:",total)
def restar_2_numero(p_num1: float,p_num2:float):
    total =p_num1 - p_num2
    print("el total de la resta es:",total)
def multiplicar_2_numero():
    num1 = float(input("ingrese primer número:"))
    num2 = float(input("ingrese segundo número"))
    total = num1 * num2
    return total
def dividir_2_numero():
    total = num1/num2
    return total
    
#########################################
print("""menu
        1. sumar 2 números
        2. restar 2 números
        3. multiplicar 2 números
        4. dividir 2 números""")
opc = int(input("ingrese opcion:"))
if opc == 1:
    suma_2_numeros
elif opc == 2:
    num1 = float(input("ingrese primer numero"))
    num2 = float(input("ingrese segundo numero"))
    restar_2_numero(num1)
elif opc == 3:
    multiplicar_2_numero()
else:
    num1 = float(input("ingrese primer numero"))
    num2 = float(input("ingrese segundo numero"))
    lista =[]
    lista.append(dividir_2_numero(num1,num2))