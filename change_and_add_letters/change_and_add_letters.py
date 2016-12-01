def pig_it(text):
    #your code here
    lista = text.split(" ")
    frase = ""
    for palavra in lista:
        if palavra.isalpha():
            frase += palavra[1:] + palavra[0] + 'ay' + ' '
        else:
            frase += palavra[0] + ' '
    return frase.rstrip()



# assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
print(pig_it('Pig latin is cool'))


"""
Melhor código:

import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)
"""