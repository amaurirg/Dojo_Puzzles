unidade = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove"} #"0":"zero",

unidezena = {"10":"dez", "11":"onze", "12":"doze", "13":"treze", "14":"quatorze", "15":"quinze", "16":"dezesseis", "17":"dezessete",
			"18":"dezoito", "19":"dezenove"}

dezena = {"2":"vinte", "3":"trinta", "4":"quarenta", "5":"cinquenta", "6":"sessenta", "7":"setenta", "8":"oitenta", "9":"noventa"}

centena = {"1":"cem", "2":"duzentos", "3":"trezentos", "4":"quatrocentos", "5":"quinhentos", 
			"6":"seiscentos", "7":"setecentos", "8":"oitocentos", "9":"novecentos"}

def digitos_1(num):
	if num == "0":
		digext = ""
	else:
		digext = unidade[num]
	return digext


def digitos_2(num):
	if num.endswith("00"):
		digext = ""
	elif num.endswith("01"):
		digext = "um"
	elif 1 < int(num) < 10:
		digext = unidade[num[1]]
	elif 10 <= int(num) < 20:
		digext = unidezena[num]
	else:
		if num.endswith("0"):
			digext = dezena[num[0]]
		else:
			digext = dezena[num[0]] + " e " + unidade[num[1]]
	return digext


def digitos_3(num):
	if num.endswith("000"):
		digext = ""
	elif num.endswith("001"):
		digext = "um"
	elif num.endswith("00"):
		digext = centena[num[0]]
	else:
		if num[:2] == "10":
			digext = "cento" + " e " + unidade[num[-1]]
		elif num[-1] != "0":
			digext = centena[num[0]] + " e " + digitos_2(num[1:])
		else:
			digext = centena[num[0]] + " e " + dezena[num[1]]
	return digext


def analisa(digitos):
	if len(digitos) == 1:
		digext = digitos_1(digitos)
	elif len(digitos) == 2:
		digext = digitos_2(digitos)
	else:
		digext = digitos_3(digitos)
	return digext
		

assert(analisa('0')) == "" 
assert(analisa('00')) == ""
assert(analisa('000')) == ""
assert(analisa('1')) == "um"
assert(analisa('4')) == "quatro"
assert(analisa('01')) == "um"
assert(analisa('10')) == "dez"
assert(analisa('50')) == "cinquenta"
assert(analisa('41')) == "quarenta e um"
assert(analisa('23')) == "vinte e três"
assert(analisa('100')) == "cem"
assert(analisa('200')) == "duzentos"
assert(analisa('320')) == "trezentos e vinte"
assert(analisa('617')) == "seiscentos e dezessete"
assert(analisa('101')) == "cento e um"
assert(analisa('701')) == "setecentos e um"

# print(analisa("617"))
