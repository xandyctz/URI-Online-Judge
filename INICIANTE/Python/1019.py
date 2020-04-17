def conversaoHora():
	total = int(input())
	
	horas = total // 3600
	restante_segundos = total - horas * 3600
	minutos = restante_segundos // 60
	segundos = restante_segundos - minutos * 60
	print('%i:%i:%i' %(horas, minutos, segundos))
	
if __name__ == '__main__':
	conversaoHora()