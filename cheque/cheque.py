# Todas as possíveis combinações
unidezena = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove",
			"01":"um", "02":"dois", "03":"três", "04":"quatro", "05":"cinco", "06":"seis", "07":"sete", "08":"oito", "09":"nove",
			"10":"dez", "11":"onze", "12":"doze", "13":"treze", "14":"quatorze", "15":"quinze", "16":"dezesseis", 
			"17":"dezessete", "18":"dezoito", "19":"dezenove"}

dezena = {"2":"vinte", "3":"trinta", "4":"quarenta", "5":"cinquenta", "6":"sessenta", "7":"setenta", "8":"oitenta", "9":"noventa"}

centena = {"1":"cento", "2":"duzentos", "3":"trezentos", "4":"quatrocentos", "5":"quinhentos", 
			"6":"seiscentos", "7":"setecentos", "8":"oitocentos", "9":"novecentos"}



# ****************** FUNÇÔES ****************** 
def dois_digitos(num_dez):
	""" Analisa as dezenas """
	if num_dez in unidezena:
		return unidezena[num_dez]
	elif num_dez[0] in dezena and num_dez[1] in unidezena:
		return dezena[num_dez[0]] + " e " + unidezena[num_dez[1]]
	else:
		# if num_dez[-1] == "0":
		return dezena[num_dez[0]]

def tres_digitos(num_cen):
	if num_cen[1:] == "00" and num_cen[0] != "0":
		return centena[num_cen[0]]
	elif num_cen == "000":
		return ""
	elif num_cen[0] == "0":
		return dois_digitos(num_cen[1:])
	else:	
		return centena[num_cen[0]] + " e " + dois_digitos(num_cen[1:])


def analisa(num):
	# Analisa se o num = 100, se é dezena ou centena
	if num == "100":
		return "cem"
	elif len(num) < 3:
		return dois_digitos(num)
	elif len(num) == 3:
		return tres_digitos(num)


def extenso(parte_reais, parte_cents):
	extreais=''
	inteiro = parte_reais.split('.')
	# print(inteiro)
	texto_reais = []
	texto_cents = ""
	for i in inteiro:
		texto_reais.append(analisa(str(i)))
	# print(extreais)
	# print(len(inteiro))
	if len(texto_reais) == 1:
		if texto_reais[-1] == "um":
			extreais = texto_reais[0] + " real"
		else:
			extreais = texto_reais[0] + " reais"
	elif len(texto_reais) == 2:
		print(texto_reais)
		if texto_reais[-1] == "":
			extreais = texto_reais[0] + " mil reais"
		if texto_reais[-1] == "um":
			extreais = texto_reais[0] + " mil e " + texto_reais[1] + " reais"
		else:
			extreais = texto_reais[0] + " mil, " + texto_reais[1] + " reais"
	elif len(texto_reais) == 3:
		if texto_reais[0] == "um":
			extreais = texto_reais[0] + " milhão, " + texto_reais[1] + " mil, " + texto_reais[2] + " reais"	
		else:
			extreais = texto_reais[0] + " milhões, " + texto_reais[1] + " mil, " + texto_reais[2] + " reais"
	else:
		extreais = texto_reais[0] + " bilhões, " + texto_reais[1] + " milhões, " + texto_reais[2] + " mil, " + texto_reais[3] + " reais"
	# print(extreais.capitalize())
	
	texto_cents = analisa(parte_cents)
	if parte_cents == "":
		extcents = "."
	elif parte_cents == "01":
		extcents = " e um centavo."
	else:
		extcents = " e " + texto_cents + " centavos."
	# print(extcents)
	texto_completo = extreais.capitalize() + extcents.capitalize()
	print(texto_completo)
	# print(texto_reais[-1])
	# texto = texto_reais + texto_cents
	# print(texto_reais, texto_cents)
	return texto_completo



	# print(texto_reais + " reais" + texto_cents)


def split1000(s, sep='.'):
	""" Separa as milhares com ponto se > 3 dígitos ou retorna o o mesmo número """
	return s if len(s) <= 3 else split1000(s[:-3], sep) + sep + s[-3:]


# ***************************************************************************

def separa(valor):
	""" Separa os reais dos centavos """
	int_cents = str(valor).split(',')
	inteiro = int_cents[0]
	centavos = int_cents[1]
	int_ponto = split1000(inteiro)
	extenso(int_ponto, centavos)
	return inteiro, centavos


# separa('192834,09')
# separa('1.234,90')
separa("1000,00")

# numero = input("Digite um valor: ")
# separa(numero)