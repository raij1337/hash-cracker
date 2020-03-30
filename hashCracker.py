#!/usr/bin/python3
import time,crypt,os,sys,colorama
from colorama import Fore

banner=""
banner+="  _    _                 _                                      _\n"
banner+=" | |  | |               | |                                    | |                        ,\n"
banner+=" | |__| |   __ _   ___  | |__       ___   _ __    __ _    ___  | | __   ___   _ __       /(  ___________\n"
banner+=" |  __  |  / _` | / __| | '_ \     / __| | '__|  / _` |  / __| | |/ /  / _ \ | '__|     |  >:===========`\n"
banner+=" | |  | | | (_| | \__ \ | | | |   | (__  | |    | (_| | | (__  |   <  |  __/ | |         )(\n"
banner+=" |_|  |_|  \__,_| |___/ |_| |_|    \___| |_|     \__,_|  \___| |_|\_\  \___| |_|         []\n"
banner+="                                                                                        HASH\n"
banner+="coded by raij\n"
print(Fore.GREEN+banner)

hash = str(input("Insira o hash: "))
salt = str(input("Insira o Salt: "))
wordlist = str(input("Wordlist: "))
arquivo = open(wordlist,encoding='utf-8', errors='replace')
senhas = arquivo.read().split('\n')

for senha in senhas:
	novo_hash = crypt.crypt(senha,salt)
	if (novo_hash == hash):
		print("\n")
		print("Senha encontrada!!! --> "+senha)
		sys.exit(0)
	else:
		print("Tentando: "+senha.strip(), end="\r")
		time.sleep(0.01)
