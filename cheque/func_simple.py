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
	

# ****************** TESTES ****************** 
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
