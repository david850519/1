#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=input('*須大於1*請輸入任一數字:')
if a>1:
	for i in range(2,a):
		if(a%i)==0:
			print ("%d不是質數")%a
			break
	else:
		print ("%d是質數")%a
else:
	print("請輸入大於一的數字")