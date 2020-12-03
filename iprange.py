#!/usr/bin/env python
# -*- coding: utf-8 -*
from socket import inet_aton, inet_ntoa
from struct import unpack, pack
from multiprocessing import Pool
from sys import argv
try: from requests import get
except: print('install requests lib (pip install requests)')
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

def work(ip):
    try:
        if get('http://'+ip, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0'}, verify=False, timeout=5, allow_redirects=False): open("IP-ALIVE.txt","a").write(ip+"\n"); print("LIVE IP > "+ip)
        else: print("IP NOT LIVE > "+ip)
    except: pass

if __name__ == '__main__':
   try:
       print("""
._____________  __________    _____    _______    _____________________________ 
|   *______   * *______   *  /  _  *   *      *  /  _____/*_   _____/*______   *
|   ||     ___/  |       _/ /  /_*  *  /   |   */   *  ___ |    __)_  |       _/
|   ||    |      |    |   */    |    */    |    *    *_*  *|        * |    |   *
|___||____|      |____|_  /*____|__  /*____|__  /*______  /_______  / |____|_  /
                        */         */         */        */        */         */ 
                    BY KTN -> USAGE : {} 1.0.0.0-255.255.255.255 (JUST AN EXEMPLE) .
                    INFO : IP RANGER + PORT 80 CHECK (USING REQUESTS LIB NOT SOCKET).
           """.format(argv[0]))
       if len(argv)==2: s,e = argv[1].split('-')
       else: s,e = raw_input("[!] PLEASE ENTER SPAN RANGE IP (EXEMPLE 1.0.0.0-1.255.255.255): ").split('-')
       ranger = lambda s,e: [inet_ntoa(pack('>I', _)) for _ in range(unpack('>I', inet_aton(s))[0], unpack('>I', inet_aton(e))[0]+1)]
       Pool(100).map(work, ranger(s,e))
       print("\nEND OF SCAN")
   except: print("\nOKAY BYE!"); exit()
