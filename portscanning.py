#!/bin/python3
import sys
import socket
from datetime import datetime

#define o alvo
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # traduz hostname para IPv4

else:
	print("\n")
	print("*" * 50)
	print("Quantidade invalida de argumentos.")
	print("Sintaxe: python3 portscanning.py <ip>")
	print("*" * 50)
	print("\n")
	sys.exit()
	
#adiciona o banner
print("-" * 50)
print("Scaneando o alvo ----> " + target)
print("tempo iniciado: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range (1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #retorna um indicador de erro
		if result == 0:
			print("Porta {} esta aberta".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nSaindo do programa.")
	sys.exit()

except socket.gaierror:
	print("Hostname nao pode ser resolvido.")

except socket.error:
	print("Nao pode conectar no servidor.")
	sys.exit()
