#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# LengLang v0.1

import os
import time
from sys import *
from dosya_ac import *
from leng2 import *
from parser import *

semboller = {}
def calis_shell():
	try:
	print("LengLang v0.1 \n")
	while True:
	veri = raw_input("<?>": ") + "\n<EOF>"
	open(".shell_data","w").write(veri)
	tokenler = leng2(veri)
	parser(tokenler,0)
	
except:
print("\n")
exit()

def calis_dosya():
	veri = dosya_ac(argv[1])
	tokenler = leng2(veri)
	parser(tokenler,0)
	
if  len(argv) == 2:
calis_dosya()
elif len(argv) == 1:
calis_shell()
else :
	print("HATA : ASIRI YUKLEME")
