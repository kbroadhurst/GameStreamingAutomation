import sys
import os

from wakeonlan import send_magic_packet

def wake_pc():
	macAddr = input("What is the MAC address of the PC to wake?")
	print("Waking PC...")
	send_magic_packet(macAddr)

def main():
	wake_pc()
	
main()

