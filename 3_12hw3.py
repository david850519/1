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

print "空白鍵共出現%d次且占%f percent"%(num,num/float(sum))
print "字母e共出現%d次且占%f percent"%(enum,enum/float(sum))

