""" Teste de função para analisar dígitos e escrever por extenso """

# Todas as possíveis combinações
unidezena = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove",
			"01":"um", "02":"dois", "03":"três", "04":"quatro", "05":"cinco", "06":"seis", "07":"sete", "08":"oito", "09":"nove",
			"10":"dez", "11":"onze", "12":"doze", "13":"treze", "14":"quatorze", "15":"quinze", "16":"dezesseis", 
			"17":"dezessete", "18":"dezoito", "19":"dezenove"}

dezena = {"2":"vinte", "3":"trinta", "4":"quarenta", "5":"cinquenta", "6":"sessenta", "7":"setenta", "8":"oitenta", "9":"noventa"}

centena = {"1":"cento", "2":"duzentos", "3":"trezentos", "4":"quatrocentos", "5":"quinhentos", 
			"6":"seiscentos", "7":"setecentos", "8":"oitocentos", "9":"novecentos"}

# ****************** FUNÇÔES ****************** 


def extenso(parte_reais, parte_cents):
	extreais=''
	inteiro = parte_reais.split('.')
	texto_reais = []
	texto_cents = ""
	for i in inteiro:
		texto_reais.append(analisa(str(i)))
	if len(texto_reais) == 1:
		if texto_reais[-1] == "um":
			extreais = texto_reais[0] + " real"
		else:
			extreais = texto_reais[0] + " reais"
	elif len(texto_reais) == 2:
		if texto_reais[-1] == "":
			extreais = texto_reais[0] + " mil reais"
		elif texto_reais[-1] == "um":
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
	
	texto_cents = analisa(parte_cents)
	# print(parte_cents)
	if parte_cents == "00":
		extcents = "."
	elif parte_cents == "01":
		extcents = " e um centavo."
	else:
		extcents = " e " + texto_cents + " centavos."
	# if 
	texto_completo = extreais.capitalize() + extcents
	print(texto_completo)
	return texto_completo


def dois_digitos(num_dez):
	""" Analisa as dezenas """
	if num_dez in unidezena:
		return unidezena[num_dez]
	elif num_dez[0] in dezena and num_dez[1] in unidezena:
		return dezena[num_dez[0]] + " e " + unidezena[num_dez[1]]
	else:
		return dezena[num_dez[0]]

def tres_digitos(num_cen):
	if num_cen[1:] == "00":
		return centena[num_cen[0]]
	elif num_cen[0] == "0":
		return dois_digitos(num_cen[1:])
	else:	
		return centena[num_cen[0]] + " e " + dois_digitos(num_cen[1:])


def analisa(num):
	# Analisa se o num = 100, se é dezena ou centena
	if num == "100":
		return "cem"
	elif num in ["0", "00", "000"]:
		return ""
	elif len(num) < 3:
		return dois_digitos(num)
	elif len(num) == 3:
		return tres_digitos(num)
	

def split1000(s, sep='.'):
	""" Separa as milhares com ponto se > 3 dígitos ou retorna o o mesmo número """
	return s if len(s) <= 3 else split1000(s[:-3], sep) + sep + s[-3:]


# ***************************************************************************

def separa(valor):
	# print(valor)
	""" Separa os reais dos centavos """
	int_cents = str(valor).split(',')
	inteiro = int_cents[0]
	centavos = int_cents[1]
	int_ponto = split1000(inteiro)
	extenso(int_ponto, centavos)
	return inteiro, centavos



# ********************************** TESTES **********************************


# Testes da função split1000(s, sep='.')
assert(split1000('100')) == '100'
assert(split1000('1000')) == '1.000'
assert(split1000('10000000')) == '10.000.000'
assert(split1000('36227110')) == '36.227.110'
assert(split1000('8374938475403')) == '8.374.938.475.403'
assert(split1000('43')) == '43'
assert(split1000('134500')) == '134.500'

# Testes com a função separa(valor)
# print(separa('3328231273,78'))
assert(separa('3328231273,78')) == ('3328231273', '78')
assert(separa('437823,34')) == ('437823', '34')
assert(separa('123,67')) == ('123', '67')
assert(separa('12341,02')) == ('12341', '02')
assert(separa('000,45')) == ('000', '45')
assert(separa('0,01')) == ('0', '01')
assert(separa('9402837498337262892,21')) == ('9402837498337262892', '21')
assert(separa('12,98')) == ('12', '98')

# Testes com a função analisa(num)
assert(analisa('1')) == "um"
assert(analisa('01')) == "um"
assert(analisa('11')) == "onze"
assert(analisa('21')) == "vinte e um"
assert(analisa('221')) == "duzentos e vinte e um"
assert(analisa('111')) == "cento e onze"
assert(analisa('101')) == "cento e um"
assert(analisa('100')) == "cem"
assert(analisa('410')) == "quatrocentos e dez"
assert(analisa('40')) == "quarenta"
assert(analisa('340')) == "trezentos e quarenta"
assert(analisa('500')) == "quinhentos"
assert(analisa('011')) == "onze"
assert(analisa('000')) == ""
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
assert(analisa('011')) == "onze"

# Testes com a função extenso
assert(extenso('1.234', '56')) == 'Um mil, duzentos e trinta e quatro reais e cinquenta e seis centavos.'
assert(extenso('1.001', '89')) == "Um mil e um reais e oitenta e nove centavos."
assert(extenso('3.576.984', '32')) == "Três milhões, quinhentos e setenta e seis mil, novecentos e oitenta e quatro reais e trinta e dois centavos."
assert(extenso('231.001', '01')) == "Duzentos e trinta e um mil e um reais e um centavo."
assert(extenso('001','01')) == "Um real e um centavo."
assert(extenso('1.011','01')) == "Um mil, onze reais e um centavo."
assert(extenso('231.011', '01')) == "Duzentos e trinta e um mil, onze reais e um centavo."
assert(extenso('1.000', '12')) == "Um mil reais e doze centavos."
assert(extenso('10.000', '00')) == "Dez mil reais."
# assert(extenso('1.000.000', '00')) == "Um milhão reais."
