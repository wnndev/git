#!/usr/bin/python
#coding:utf-8
# 检查网络连通性
import urllib
import time
import RPi.GPIO as GPIO 
import os
def check_network():
	i=0
	while 1:
		try:
			result=urllib.urlopen('http://baidu.com').read()
			#print result
			print "Network is Ready!"
			break
		except Exception , e:
			#print e
			print "Network is not ready,Sleep 5s...."
			time.sleep(5)
			i=i+1;
			if i>5:
				i=0
				return False
	return True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11,GPIO.IN)

while 1:
	mode=GPIO.input(11)
	if mode==1:	
		print "running"
		a=check_network()
		if a==False:
			os.system("reboot")
		else:
			time.sleep(25)
	else:
		print "debug"
		time.sleep(30)

