def calcula_idade(ano_atual, ano_nascimento):
    """
    calcula idade conforme o ano atual e ano de nascimento
    :param ano_atual:  o ano atual
    :param ano_nascimento: o ano de nascimento
    :return: idade conforme o ano de nascimento
    """
    idade = ano_atual - ano_nascimento
    return idade


def kelin(celsius):
    """
    calcula o kelin conforme a temperatura em celsius
    :param celsius: a temperatura em celsius
    :return:transforma temperatura em celsius em Kelin
    """
    kelin = celsius + 273.15
    return kelin

def fahrente(celsius):
    """
    calcula o fahrente conforme a temperatura em celsius
    :param celsius: a temperatura em celsius
    :return: transforma temperatura em celsius em Fahrente
    """
    fahrente = celsius * 1.8 + 32
    return fahrente

def menu_calculadora():
    """
    mostra o menu calculadora
    :return: o menu da calculadora
    """
    print("calculadora")
    print("1 - soma\n2 - subtração\n3- multiplicação\n4 - divisão\n5 - todas as contas")

def soma(numero1, numero2):
    """
    soma o numero1 e o numero2
    :param numero1: primeiro numero
    :param numero2: segundo numero
    :return: soma dos numeros
    """
    return numero1 + numero2
def subtracao(numero1, numero2):
    """
    subtrai o numero1 e o numero2
    :param numero1: primeiro numero
    :param numero2: segundo numero
    :return: subtração dos numeros
    """
    return numero1 - numero2
def multiplicacao(numero1, numero2):
    """
    multiplica o numero1 e o numero2
    :param numero1: primeito do numero
    :param numero2: segundo do numero
    :return: multiplicacao dos numeros
    """
    return numero1 * numero2


def divisao(numero1, numero2):
    """
    realiza a divisão do numero1 e do numero2
    :param numero1: primeito do numero1
    :param numero2: segundo numero
    :return: divisão dos numeros
    """
    return numero1 / numero2


def escolhas(escolha,numero1, numero2):
    """
    escolhe qual operação sera realizada
    :param escolha: escolha
    :param numero1: numero1
    :param numero2: numero2
    :return: o resultado da operação que foi escolhida
    """
    if escolha == 1:
        print("soma", soma(numero1, numero2))
    elif escolha == 2:
        print("subtração", subtracao(numero1, numero2))
    elif escolha == 3:
        print("multiplicação", multiplicacao(numero1, numero2))
    elif escolha == 4:
        print("divisao", divisao(numero1, numero2))
    else:
        print("escolha invalida")



def imc(altura1, peso1):
    """
    calcula o imc conforme a altura e peso
    :param altura1: altura
    :param peso1: peso
    :return: o imc conforme altura e peso
    """
    return peso1 / (altura1 * altura1)

