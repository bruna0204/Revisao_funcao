from utils.math_utils import *


ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
print("Voce tem", calcula_idade(ano_atual= ano_atual, ano_nascimento= ano_nascimento),"anos")
celsius = int(input("Digite o valor da celsius: "))
print("O valor em Kelvin é", kelin(celsius=celsius))
print("O valor em fahrent é", fahrente(celsius=celsius))




numero1 = int(input("Digite o primeito numero: "))
numero2 = int(input("Digite o segundo numero: "))
menu_calculadora()
escolha = int(input("digite sua escolha: "))
escolhas(escolha=escolha,numero1=numero1, numero2=numero2)


peso1 = float(input("Digite o primeito peso: "))
altura1 = float(input("Digite sua altura: "))

print("Seu IMC é", imc(peso1=peso1, altura1=altura1))