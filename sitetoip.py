#!/usr/bin/env python
# -*- coding: utf-8 -*

from socket import gethostbyname
from urlparse import urlparse
from multiprocessing.dummy import Pool
from sys import argv

def ip(url):
	try:
		print("GETING IP FROM -> "+url)
		if not urlparse(url).scheme: url = urlparse('http://'+url).netloc
		else: url = urlparse(url).netloc
		open("IPS.txt","a").write(str(gethostbyname(url))+"\n")
	except: pass

if __name__ == '__main__':
	try:
		with open(argv[1]) as f: urls = f.read().splitlines()
		Pool(20).map(ip, urls)
	except: print("USAGE =-> {} list-site.txt".format(argv[0]))