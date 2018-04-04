# Definir funcion de fibonnacci

def Fibo (N):
	#caso base
	if (N==0 && N==1):
		return N;
	#segundo caso
	else
		return Fibo (N-2)+ Fibo (N-1)
	
