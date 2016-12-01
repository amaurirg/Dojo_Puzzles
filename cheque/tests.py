unidade = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove"}  #"0":"zero", 

unidezena = {"10":"dez", "11":"onze", "12":"doze", "13":"treze", "14":"quatorze", "15":"quinze", "16":"dezesseis", "17":"dezessete",
			"18":"dezoito", "19":"dezenove"}

dezena = {"2":"vinte", "3":"trinta", "4":"quarenta", "5":"cinquenta", "6":"sessenta", "7":"setenta", "8":"oitenta", "9":"noventa"}

centena = {"1":"cem", "2":"duzentos", "3":"trezentos", "4":"quatrocentos", "5":"quinhentos", 
			"6":"seiscentos", "7":"setecentos", "8":"oitocentos", "9":"novecentos"}



def extenso(parte_inteiro, parte_centavos):
	# print("inteiro: ", parte_inteiro)
	# print("centavos: ", parte_centavos)
	if int(parte_centavos) == 0:
		centavos = "."
	elif (parte_centavos) == "01":
		centavos = " e um centavo."
	elif 1 < int(parte_centavos) < 10:
		centavos = " e " + unidade[parte_centavos[1]] + " centavos."
	elif 10 <= int(parte_centavos) < 20:
		centavos = " e " + unidezena[parte_centavos] + " centavos."
	else:
		if parte_centavos[1] != "0":
			centavos = " e " + dezena[parte_centavos[0]] + " e " + unidade[parte_centavos[1]] + " " + "centavos."
		else:
			centavos = " e " + dezena[parte_centavos[0]] + " " + "centavos."
	print(centavos)
	inteiro = parte_inteiro.split('.')
	# print(inteiro[-1])
	# print(len(inteiro))
	for i, num in enumerate(inteiro[::-1]):
		if i < (len(inteiro)-1):
			print(num)
		else:
			print(unidade[num])
		# num[0]
	# print(inteiro)
	# return 'Um mil e duzentos e trinta e quatro reais e cinquenta e seis centavos'


def split1000(s, sep='.'):
	""" Separa as milhares com ponto se > 3 dígitos ou retorna o o mesmo número """
	# print (s[-3:])
	return s if len(s) <= 3 else split1000(s[:-3], sep) + sep + s[-3:]

# Função sem ListComprehension
# def split1000(s, sep='.'):
# 	if len(s) <= 3:
# 		return s  
# 	else:
# 		return split1000(s[:-3]) + sep + s[-3:]

# ***************************************************************************

def separa(valor):
	""" Separa os reais dos centavos """
	int_cents = str(valor).split(',')
	inteiro = int_cents[0]
	centavos = int_cents[1]
	# print("inteiro: ",inteiro)
	# print("centavos: ", centavos)
	# print(split1000(inteiro))
	int_ponto = split1000(inteiro)
	print("int_ponto = ", int_ponto)
	extenso(int_ponto, centavos)
	return inteiro, centavos

# ********************************** TESTES **********************************

"""
# Testes da função split1000(s, sep='.')
assert(split1000('100')) == '100'
assert(split1000('1000')) == '1.000'
assert(split1000('10000000')) == '10.000.000'
assert(split1000('36227110')) == '36.227.110'
assert(split1000('8374938475403')) == '8.374.938.475.403'
assert(split1000('43')) == '43'
assert(split1000('134500')) == '134.500'
"""

"""
# Testes com a função separa(valor)
# print(separa('3328231273,78'))
assert(separa('3328231273,78')) == ('3328231273', '78')
assert(separa('437823,34')) == ('437823', '34')
assert(separa('123,67')) == ('123', '67')
assert(separa('10000,00')) == ('10000', '00')
assert(separa('9402837498337262892,21')) == ('9402837498337262892', '21')
assert(separa('12,98')) == ('12', '98')
"""


# Testes com a função extenso
# assert(extenso('1234', '56')) == 'Um mil e duzentos e trinta e quatro reais e cinquenta e seis centavos'


separa('9402837498337262892,21')