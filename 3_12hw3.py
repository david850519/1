#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open('input.txt','r')
num=0
enum=0
line=f.read()
for i in range(0,len(line)):
	if(line[i]==' '):
		num=num+1
	if(line[i]=='e'):
		enum=enum+1
sum=len(line)

print "�ť���@�X�{%d���B�e%f percent"%(num,num/float(sum))
print "�r��e�@�X�{%d���B�e%f percent"%(enum,enum/float(sum))

