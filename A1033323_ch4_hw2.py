#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
num=random.randrange(1,99,1)
a=input('�׷��K�X�C���A�вq1~99�������Ʀr:\n')
sum=1
max=99
min=1
while(a!=num):
	if(a<num):
		min=a
		print "�����F�A�{�b���d��%d~%d"%(a,max)
		a=input('�п�J�d�򤺪��Ʀr')
		sum=sum+1
	if(a>num):
		max=a
		print "�����F�A�{�b���d��%d~%d"%(min,a)
		a=input('�п�J�d�򤺪��Ʀr')
		sum=sum+1
print "���߱z����F!!�z�@��F�q�F%d��"%sum


