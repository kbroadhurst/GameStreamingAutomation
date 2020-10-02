import sys
import os
import cec

from wakeonlan import send_magic_packet

def wake_pc():
	macAddr = os.environ['WOL_MAC'] if ("WOL_MAC" in os.environ) else input("What is the MAC address of the PC to wake?")
	print("Waking PC...")
	send_magic_packet(macAddr)

def wake_tv():
	cec.init()
	tv = cec.Device(0)
	tv.power_on()

def main():
	wake_pc()
	wake_tv()
	
main()

