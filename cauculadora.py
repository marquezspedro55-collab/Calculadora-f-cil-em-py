# -------------------------------
# CALCULADORA COMPLETA EM PYTHON
# Aproximadamente 200 linhas
# -------------------------------

import math
import time

historico = []

def linha():
    print("-" * 40)

def titulo():
    linha()
    print("        CALCULADORA PYTHON")
    linha()

def menu():
    print("\nEscolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Porcentagem")
    print("8 - Média de números")
    print("9 - Mostrar histórico")
    print("10 - Limpar histórico")
    print("0 - Sair")

def pedir_numero(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except:
            print("Digite um número válido.")

def salvar_historico(conta):
    historico.append(conta)

def soma():
    linha()
    print("SOMA")
    linha()
    a = pedir_numero("Primeiro número: ")
    b = pedir_numero("Segundo número: ")
    resultado = a + b
    conta = f"{a} + {b} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def subtracao():
    linha()
    print("SUBTRAÇÃO")
    linha()
    a = pedir_numero("Primeiro número: ")
    b = pedir_numero("Segundo número: ")
    resultado = a - b
    conta = f"{a} - {b} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def multiplicacao():
    linha()
    print("MULTIPLICAÇÃO")
    linha()
    a = pedir_numero("Primeiro número: ")
    b = pedir_numero("Segundo número: ")
    resultado = a * b
    conta = f"{a} * {b} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def divisao():
    linha()
    print("DIVISÃO")
    linha()
    a = pedir_numero("Primeiro número: ")
    b = pedir_numero("Segundo número: ")

    if b == 0:
        print("Não pode dividir por zero.")
        return

    resultado = a / b
    conta = f"{a} / {b} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def potencia():
    linha()
    print("POTÊNCIA")
    linha()
    base = pedir_numero("Base: ")
    expoente = pedir_numero("Expoente: ")
    resultado = base ** expoente
    conta = f"{base} ^ {expoente} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def raiz():
    linha()
    print("RAIZ QUADRADA")
    linha()
    num = pedir_numero("Número: ")

    if num < 0:
        print("Não existe raiz de número negativo.")
        return

    resultado = math.sqrt(num)
    conta = f"√{num} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def porcentagem():
    linha()
    print("PORCENTAGEM")
    linha()
    valor = pedir_numero("Valor: ")
    porcento = pedir_numero("Porcentagem (%): ")
    resultado = valor * (porcento / 100)
    conta = f"{porcento}% de {valor} = {resultado}"
    print("Resultado:", resultado)
    salvar_historico(conta)

def media():
    linha()
    print("MÉDIA DE NÚMEROS")
    linha()

    quantidade = int(pedir_numero("Quantos números? "))

    soma_total = 0

    for i in range(quantidade):
        n = pedir_numero(f"Número {i+1}: ")
        soma_total += n

    resultado = soma_total / quantidade
    conta = f"Média de {quantidade} números = {resultado}"

    print("Resultado:", resultado)
    salvar_historico(conta)

def mostrar_historico():
    linha()
    print("HISTÓRICO")
    linha()

    if len(historico) == 0:
        print("Nenhuma conta ainda.")
    else:
        for item in historico:
            print(item)

def limpar_historico():
    historico.clear()
    print("Histórico apagado.")

def sair():
    linha()
    print("Encerrando calculadora...")
    time.sleep(1)
    print("Até logo!")

def executar(opcao):

    if opcao == "1":
        soma()

    elif opcao == "2":
        subtracao()

    elif opcao == "3":
        multiplicacao()

    elif opcao == "4":
        divisao()

    elif opcao == "5":
        potencia()

    elif opcao == "6":
        raiz()

    elif opcao == "7":
        porcentagem()

    elif opcao == "8":
        media()

    elif opcao == "9":
        mostrar_historico()

    elif opcao == "10":
        limpar_historico()

    elif opcao == "0":
        sair()

    else:
        print("Opção inválida.")

def main():

    titulo()

    while True:

        menu()

        opcao = input("\nDigite a opção: ")

        if opcao == "0":
            sair()
            break

        executar(opcao)

        input("\nPressione ENTER para continuar...")
        print("\n" * 3)

# execução do programa
main()