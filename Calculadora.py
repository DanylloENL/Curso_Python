print("\n******************* Python Calculator *******************")
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return  num1 - num2

def multi(num1, num2):
    return num1 * num2

def divi (num1, num2):
    return  num1 / num2

print("\nSelecione o número da operação desejada: \n")

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

resultado = input("Digite sua opção (1/2/3/4): ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if resultado == '1':

    print(f"O valor da operação {num1} + {num2} é: ", add(num1, num2))

elif resultado == '2':

    print(f"O valor da operação {num1} - {num2} é:", sub(num1, num2))

elif resultado == '3':

    print(f"O valor da operação {num1} * {num2} é:", multi(num1, num2))

elif resultado == '4':

    print(f"O valor da operação {num1} / {num2} é: ", divi(num1, num2))

else:
    print("Número fora da listagem informada. Por favor, tente novamente!")
