#!/usr/bin/python
#coding:utf-8
import os
def getCPUfreq():
    freq=os.popen('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq').readline().strip()
    freq=freq[:-3]+' MHz'	
    return(freq) 
# Return CPU temperature as a character string                                     
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n"," 'C"))
 
# Return RAM information (unit=kb) in a list                                      
# Index 0: total RAM                                                              
# Index 1: used RAM                                                                
# Index 2: free RAM                                                                
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
 
# Return % of CPU used by user as a character string                               
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
 
# Return information about disk space as a list (unit included)                    
# Index 0: total disk space                                                        
# Index 1: used disk space                                                        
# Index 2: remaining disk space                                                    
# Index 3: percentage of disk used                                                 
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
 
 
# CPU informatiom
CPU_freq = getCPUfreq()
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()
 
# RAM information
# Output is in kb, here I convert it in Mb for readability
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)
 
# Disk information
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_used = DISK_stats[1]
DISK_perc = DISK_stats[3]
 
if __name__ == '__main__':
    print('')
    print('CPU frequency = '+CPU_freq)
    print('CPU Temperature = '+CPU_temp)
    print('CPU Use = '+CPU_usage+' %')
    print('')
    print('RAM Total = '+str(RAM_total)+' MB')
    print('RAM Used = '+str(RAM_used)+' MB')
    print('RAM Free = '+str(RAM_free)+' MB')
    print('') 
    print('DISK Total Space = '+str(DISK_total)+'B')
    print('DISK Used Space = '+str(DISK_used)+'B')
    print('DISK Used Percentage = '+str(DISK_perc))

p=os.popen("netstat –apn | grep ssh")
a=1
line=p.read().replace("ESTABLISHED","花生壳")
st=line.split("\n")
item=len(st)-1
str=[]
if item<0:
        print "no ssh"
        exit()
for i in range(0,item):
        str.append(st[i].split("ssh      ")[1].split(" ")[0])
print "\nSSH连接来自"
for i in range(0,item):
        print "%d: "%(i+1) + str[i]
print " "

