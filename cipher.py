ed = input("Digite 1 para criptografar e 2 para descriptografar\n")

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

arqv = open("texto.txt", "r")

texto = str(arqv.readlines())

texto = texto.replace("[", "")
texto = texto.replace("'", "")
texto = texto.replace("]", "")

arqvout = open("encryptedcesar.txt","r+")

if(ed == '1'):
	texto = texto.lower()
	texto2 = ''
	deslocamento = int(input("Digite o modulo de deslocamento desejado\n"))
	for x in texto:
		if(x.isalpha()):
			indice = alfabeto.index(x)
			if(indice+deslocamento >= len(alfabeto)):
				texto2 += alfabeto[((indice+deslocamento)) - 26]
			else:
				texto2 += alfabeto[(indice+deslocamento)]
		else:
			texto2 += x
	print(texto2)
	arqvout.write(texto2)	


if(ed == '2'):
	decryption = str(arqvout.readlines())
	decryption = decryption.lower()
	decryption = decryption.replace("[", "")
	decryption = decryption.replace("'", "")
	decryption = decryption.replace("]", "")
	texto2 = ''
	deslocamento = int(input("Digite o modulo de deslocamento desejado\n"))
	for x in decryption:
		if(x.isalpha()):
			indice = alfabeto.index(x)
			if(indice-deslocamento < 0):
				texto2 += alfabeto[(indice-deslocamento) + 26]
			else:
				texto2 += alfabeto[(indice-deslocamento)]
		else:
			texto2 += x
	print(texto2)

arqv.close()
arqvout.close()
