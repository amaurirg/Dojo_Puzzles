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
		# print(texto_reais)
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
	# print(texto_completo)
	return texto_completo