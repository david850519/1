<<<<<<< HEAD
# -*- coding: utf-8 -*-
f =open("ATM.txt","w")
print "Hello!What's your name"
name=raw_input()
print "Hello!%s how much do you want?" %name
take=input()
a=5000
b=5000-take
if(b<0):
	print("sorry your money isn't enough")
	f.write("sorry your money isn't enough")
if(b==0):
	print("okay,but you have no money now")
	f.write("okay,but you have no money now")
if(b>0):
	print("okay,you still have %d money") %b
	f.write(("okay,you still have %d money") %b)
	f.close()
=======
hello world


hello python
>>>>>>> 85e946cc550a4ce342a62013f1221b7e5fb46dc3
