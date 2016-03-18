#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
num=random.randrange(1,99,1)
a=input('終極密碼遊戲，請猜1~99之間的數字:\n')
sum=1
max=99
min=1
while(a!=num):
	if(a<num):
		min=a
		print "答錯了，現在的範圍為%d~%d"%(a,max)
		a=input('請輸入範圍內的數字')
		sum=sum+1
	if(a>num):
		max=a
		print "答錯了，現在的範圍為%d~%d"%(min,a)
		a=input('請輸入範圍內的數字')
		sum=sum+1
print "恭喜您答對了!!您共花了猜了%d次"%sum


