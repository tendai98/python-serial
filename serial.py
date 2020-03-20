#!/usr/bin/python3

import serial
import sys
from scapy.all import hexdump

dev = serial.Serial()
buffer = b""
data = b""

try:
	dev.port = sys.argv[1]
	dev.baudrate = int(sys.argv[2])
	dev.open()
	while True:
		try:
			data = dev.read()
			buffer += data

			if data == b"\n":
				sys.stdout.write(buffer.decode())
				buffer = b""
				data = b""
		except Exception as e:
			hexdump(buffer)
			print("[!] INTERRUPT -> {}".format(e))
			exit(0)
except IndexError:
	print("Usage: {} {} {}".format(sys.argv[0],"<port>","<speed>"))


except Exception as e:
	print(e)
