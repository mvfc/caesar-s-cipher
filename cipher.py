ed = input("Digite 1 para criptografar e 2 para descriptografar\n")

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if(ed == '1'):
	texto = input("Digite o que deseja que seja criptografado\n")
	texto = texto.lower()
	texto2 = ''
	deslocamento = int(input("Digite o modulo de deslocamento desejado\n"))
	for x in texto:
		if(x.isalpha()):
			indice = alfabeto.index(x)
			texto2 += alfabeto[((indice+deslocamento))]
		else:
			texto2 += x
	print(texto2)

if(ed == '2'):
	texto = input("Digite o que deseja que seja criptografado\n")
	texto = texto.lower()
	texto2 = ''
	deslocamento = int(input("Digite o modulo de deslocamento desejado\n"))
	for x in texto:
		if(x.isalpha()):
			indice = alfabeto.index(x)
			texto2 += alfabeto[((indice-deslocamento))]
		else:
			texto2 += x
	print(texto2)
