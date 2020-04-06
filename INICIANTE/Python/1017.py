tempo_gasto = int(input())
velocidade_media = int(input())

def combustivel():
	resultado = (tempo_gasto * velocidade_media) / 12
	print('%.3f' %resultado)
combustivel()