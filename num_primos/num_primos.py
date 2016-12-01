"""
Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.
Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.
Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.
>>> palavra_prima('b')
True
>>> palavra_prima('d')
False
>>> palavra_prima('C')
True
>>> palavra_prima('B')
False
>>> palavra_prima('grupy')
True
>>> palavra_prima('aaaa')
False
>>> palavra_prima('aaa')
True
>>> palavra_prima('a')
False
>>> palavra_prima('CB')
False
>>> palavra_prima('G')
False
>>> soma_palavra('A')
26
>>> soma_palavra('aaaa')
4
"""
import string

#print(letras)
#letras = [ord(str(x) for x in range(97, 123)]

#print(letras)
def palavra_prima(palavra):
    soma = soma_palavra(palavra)
    if soma <= 1:
        return False

    for i in range(1,soma-1):
        if soma%i == 0:
            return False

    return True
    # soma_palavra(palavra) //

def numero_primo(num):
    if num == 0: return "Não pode ser igual zero"
    cont = 0
    while cont < 2:
        for i in range(1,num+1):
            if num % i == 0:
                cont += 1
                print (cont)
    if cont == 2: return "Número Primo"
    else: return "Não é Número Primo"


    # return

def retorna_numero(letra):
    return string.ascii_letters.index(letra) + 1

def soma_palavra(palavra):
    return sum([retorna_numero(letra) for letra in palavra])


assert retorna_numero('a') == 1
assert retorna_numero('e') == 5
assert retorna_numero('Z') == 52

assert soma_palavra('aa') == 2
assert soma_palavra('abc') == 6
assert soma_palavra('Grupy') == 113

assert palavra_prima('aa')

print(numero_primo(2351))
print(numero_primo())


