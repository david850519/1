#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=input('*���j��1*�п�J���@�Ʀr:')
if a>1:
	for i in range(2,a):
		if(a%i)==0:
			print ("%d���O���")%a
			break
	else:
		print ("%d�O���")%a
else:
	print("�п�J�j��@���Ʀr")