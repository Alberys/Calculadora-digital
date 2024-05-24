# Passo 1: Criar Funções para Operações Matemáticas

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y

# Passo 2: Estruturando o Programa Principal

def mostrar_menu():
    print("\nEscolha a operação desejada:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    while True:
        mostrar_menu()
        
        escolha = input("Digite a opção (1/2/3/4/5): ")
        
    
        
        if escolha in ['1', '2', '3', '4']:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

