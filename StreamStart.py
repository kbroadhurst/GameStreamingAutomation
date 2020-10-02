import sys
import os
import cec
import subprocess

from wakeonlan import send_magic_packet

def wake_pc():
	macAddr = os.environ['WOL_MAC'] if ("WOL_MAC" in os.environ) else input("What is the MAC address of the PC to wake?")
	print("Waking PC...")
	send_magic_packet(macAddr)

def wake_tv():
	tv = cec.Device(0)
	print("Turning on TV...")
	tv.power_on()

def stream_games():
	print("Starting streaming service...")
	result = subprocess.call(['moonlight', 'stream', '-1080'])

def turn_off_tv():
	tv = cec.Device(0)
	print("Turning off TV...")
	tv.standby()

def main():
	cec.init()
	wake_pc()
	wake_tv()
	stream_games()
	turn_off_tv()
	
main()

