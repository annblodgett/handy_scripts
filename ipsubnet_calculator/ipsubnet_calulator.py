# Calculator for CIDR based IPv4 Subnetting
# Returns the Network Mask, Network Address, First Host Address, Last host Address, Broadcast Address, Number of Hosts. Each is in dot decimal form. Values can be anywhere from 0.0.0.0 through 255.255.255.255.

#---------- BEGIN CODE ----------#
#--Import needed modules--#
import math
#--User Input--#
	#Get User to type in the IP address divided by octets -- firstOct, secondOct, thirdOct, fourthOct- and CIDR slash-value - cidrValue.
firstOct= input('enter the first octet value: ')
secondOct= input('enter the second octet value: ')
thirdOct= input('enter the third octet value: ')
fourthOct= input('enter the fourth octet value: ')
cidrValue= input('enter the value that comes after the /:  ')
print "The value you entered was "+str(firstOct)+ "."+str(secondOct)+"."+str(thirdOct)+"."+str(fourthOct)+"/"+str(cidrValue)+" "
#--Return Network Mask--#
	#Convert CIDR notation to dot decimal netmask. This returns the Network Mask.
	# ADD CALC HERE
	# Print the Network Mask to console.
# -- Return the Network Address --#
# Get the multiplication/division factor -mdf- ( can be 128,64,32,16,8,4,2 or 1) and the workingOctet value (can be 1-4) based on the CIDR value .
# If the cidrValue is <= 8 then the mdf options are 128,64,32,16,8,4,2 and 1 . We are in working the first octet. octetValue=0 
if cidrValue <= 8:
	workingOctet=1
	if cidrValue==1:
		mdf=128
	if cidrValue==2:
		mdf=64
	if cidrValue==3:
		mdf=32
	if cidrValue==4:
		mdf=16
	if cidrValue==5:
		mdf=8
	if cidrValue==6:
		mdf=4
	if cidrValue==7:
		mdf=2
	if cidrValue==8:
		mdf=1
	print "mdf is "+ str(mdf)+"."
	print "we are working in octet number "+str(workingOctet)+"."
# If the cidrValue is greater than 8 
if cidrValue > 8:
	#To get the workingOctet take the whole # part of the cidrValue/8. Each full whole number (1,2 etc.) represents a full octet so octetValue=1 is 255.x.x.x  working in the 2nd octet. If octetValue is 2 we are working in the 3rd octet which is 255.255 etc. 
	# The workingOctet value is n+1 where n is the whole # (int) part of the cidrValue/8
	workingOctet=int(cidrValue/8)+1
	print "We are working in octet number "+str(workingOctet)+"."
	# Then to get the mdf take the cidrValue%8 (remainder) and the number should be an int value between 1-7 which corresponds to mdf options are 128,64,32,16,8,2 and 1 descending.
	if cidrValue%8==1:
		mdf=128
	if cidrValue%8==2:
		mdf=64
	if cidrValue%8==3:
		mdf=32
	if cidrValue%8==4:
		mdf=16
	if cidrValue%8==5:
		mdf=8
	if cidrValue%8==6:
		mdf=4
	if cidrValue%8==7:
		mdf=2
	if cidrValue%8==8:
		mdf==1
	print "mdf is "+ str(mdf)+"."
# Define the calcValue function.
# First the workingOctet number cooresponds to the firstOct, secondOct, thirdOct and fourthOct respectively. That user entered value then becomes the startNumber.
def calcValue(n):
	if n==1:
		startNumber = firstOct
	if n==2:
		startNumber = secondOct
	if n == 3:
		startNumber = thirdOct
	if n == 4:
		startNumber = fourthOct
	# divide the mdf by startNumber . 
	dcValue = float(startNumber/mdf)
	#We only want the whole number part. this becomes the wnValue (stands for whole number value).
	wnValue = int(dcValue//1)
	# multiply the wnValue by the mdf.  This value is becomes netFirstValue.
	global netFirstValue
	netFirstValue= wnValue*mdf
	# multiply (wnValue+1) by the mdf. Then -1 from that value.  This becomes the lastBroadcastValue.
	global lastBroadcastValue
	lastBroadcastValue = ((wnValue+1)*mdf)-1	
# Define networkAddress function. Create cases based on the workingOctet value. naXOct stands for network address (ordinal number) Octet. 
def networkAddress():
	# If workingOctet = 1 naSecondOct, naThirdOct,and naFourthOct should be 0. naFirstOct is determined by the calcValue function. It is the netFirstValue. 
	if workingOctet ==1:
		calcValue(1)
		naFirstOct =netFirstValue
		naSecondOct =0
		naThirdOct =0
		naFourthOct =0
		print "The network address is "+str(naFirstOct)+ "."+str(naSecondOct)+"."+str(naThirdOct)+"."+str(naFourthOct)+" "	
	# If workingOctet = 2 naFirstOct should be the user entered values for firstOct while naThirdOct and naFourthOct should be 0. naSecondOct is determined by the calcValue function . It is the net.firstValue. 
	if workingOctet ==2:
		calcValue(2)
		naFirstOct =firstOct
		naSecondOct =netFirstValue
		naThirdOct =0
		naFourthOct =0
		print "The network address is "+str(naFirstOct)+ "."+str(naSecondOct)+"."+str(naThirdOct)+"."+str(naFourthOct)+" "		
	# If workingOctet = 3 naFirstOct and naSecondOct should be user entered values for firstOct and secondOct while naFourthOct should be 0. naThirdOct is determined by the calcValue function. It is the net.firstValue. 
	if workingOctet ==3:
		calcValue(3)
		naFirstOct =firstOct
		naSecondOct =secondOct
		naThirdOct =netFirstValue
		naFourthOct = 0	
		print "The network address is "+str(naFirstOct)+ "."+str(naSecondOct)+"."+str(naThirdOct)+"."+str(naFourthOct)+" "
	# If workingOctet = 4 naFirstOct, naSecondOct and naThirdOct are all user entered values for firstOct, secondOct, and thirdoct. naFourthOct is determined by the calcValue function. It is the net.firstValue. 
	if workingOctet ==4:
		calcValue(4)
		naFirstOct=firstOct
		naSecondOct=secondOct
		naThirdOct=thirdOct
		naFourthOct=netFirstValue
		print "The network address is "+str(naFirstOct)+ "."+str(naSecondOct)+"."+str(naThirdOct)+"."+str(naFourthOct)+" "
# Print the Network Address to console. It should be in the form naFirstOct.naSecondOct.naThirdOct.naFourthOct.
networkAddress()
#--Return the First Host Address--#
# Create cases based on the workingOctet value. fhXOct stands for first host (ordinal number) Octet. 
def firstHostAddress():	
	# If workingOctet = 1 fhSecondOct, fhThirdOct should be 0,and fhFourthOct should be 1. fhFirstOct is determined by the calcValue function. It is the net.firstValue. 
	if workingOctet ==1:
		calcValue(1)
		fhFirstOct =netFirstValue
		fhSecondOct =0
		fhThirdOct =0
		fhFourthOct =1
		print "The network address is "+str(fhFirstOct)+ "."+str(fhSecondOct)+"."+str(fhThirdOct)+"."+str(fhFourthOct)+" "
	# If workingOctet = 2 fhFirstOct should should be the user entered values for firstOct while fhThirdOct should be 0 and fhFourthOct should be 1. fhSecondOct is determined by the calcValue function . It is the net.firstValue. 
	if workingOctet ==2:
		calcValue(2)
		fhFirstOct =firstOct
		fhSecondOct =netFirstValue
		fhThirdOct =0
		fhFourthOct =1
		print "The network address is "+str(fhFirstOct)+ "."+str(fhSecondOct)+"."+str(fhThirdOct)+"."+str(fhFourthOct)+" "
	# If workingOctet = 3 fhFirstOct and fhSecondOct should be should be the user entered values for firstOct abd secondOct while fhFourthOct should be 1. fhThirdOct is determined by the calcValue function. It is the net.firstValue. 
	if workingOctet ==3:
		calcValue(3)
		fhFirstOct =firstOct
		fhSecondOct =secondOct
		fhThirdOct =netFirstValue
		fhFourthOct =1
		print "The network address is "+str(fhFirstOct)+ "."+str(fhSecondOct)+"."+str(fhThirdOct)+"."+str(fhFourthOct)+" "
	# If workingOctet = 4 fhFirstOct, fhSecondOct and fhThirdOct are all should be the user entered values for firstOct, secondOct and thirdOct. fhFourthOct is determined by the calcValue function. (It is the net.firstValue+1)
	if workingOctet ==4:
		calcValue(4)
		fhFirstOct=firstOct
		fhSecondOct=secondOct
		fhThirdOct =thirdOct
		fhFourthOct=(netFirstValue+1)
		print "The first host address is "+str(fhFirstOct)+ "."+str(fhSecondOct)+"."+str(fhThirdOct)+"."+str(fhFourthOct)+" "
# Print the First Host Address to console. It should be in the form fhFirstOct.fhSecondOct.fhThirdOct.fhFourthOct.
firstHostAddress()	
#--Return the Last host Address--#
# Create cases based on the workingOctet value. lhXOct stands for last host (ordinal number) Octet.
def lastHostAddress(): 
	# If workingOctet = 1 lhSecondOct, lhThirdOct,should be 255 lhFourthOct should be 254. lhFirstOct is determined by the calcValue function. It is the last.broadcastValue. 
	if workingOctet ==1:
		calcValue(1)
		lhFirstOct =lastBroadcastValue
		lhSecondOct=255
		lhThirdOct =255
		lhFourthOct=254
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
	# If workingOctet = 2 lhFirstOct the user entered values for firstOct and  lhThirdOct should be 255 and lhFourthOct should be 254. lhSecondOct is determined by the calcValue function . It is the last.broadcastValue.  
	if workingOctet ==2:
		calcValue(2)
		lhFirstOct=firstOct
		lhSecondOct=lastBroadcastValue
		lhThirdOct=255
		lhFourthOct=254
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
	# If workingOctet = 3 lhFirstOct and lhSecondOct should be the user entered values for firstOct and secondOct while lhFourthOct should be 254. lhThirdOct is determined by the calcValue function. It is the last.broadcastValue. 
	if workingOctet ==3:
		calcValue(3)
		lhFirstOct=firstOct
		lhSecondOct=secondOct
		lhThirdOct=lastBroadcastValue
		lhFourthOct=254
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
	# If workingOctet = 4 lhFirstOct, lhSecondOct and lhThirdOct are all the user entered values for firstOct, secondOct and thirdoct. lhFourthOct is determined by the calcValue function. It is the last.broadcastValue.-1
	if workingOctet ==4:
		calcValue(4)
		lhFirstOct=firstOct
		lhSecondOct=secondOct
		lhThirdOct=thirdOct
		lhFourthOct=(lastBroadcastValue-1)
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
# Print the Last host Address to console. It should be in the form lhFirstOct.lhSecondOct.lhThirdOct.lhFourthOct.
lastHostAddress()
#--Return the Broadcast Address--#
# Create cases based on the workingOctet value. baXOct stands for broadcast address (ordinal number) Octet. 
def broadcastAddress ():
	# If workingOctet = 1 baSecondOct, baThirdOct and baFourthOct should be 255. baFirstOct is determined by the calcValue function. It is the last.broadcastValue. 
	if workingOctet ==1:
		calcValue(1)
		lhFirstOct =lastBroadcastValue
		lhSecondOct=255
		lhThirdOct =255
		lhFourthOct=255
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "
	# If workingOctet = 2 baFirstOct the user entered values for firstOct and  baThirdOct and baFourthOct should be 255. baSecondOct is determined by the calcValue function . It is the last.broadcastValue.  
	if workingOctet ==2:
		calcValue(2)
		lhFirstOct=firstOct
		lhSecondOct=lastBroadcastValue
		lhThirdOct=255
		lhFourthOct=255
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
	# If workingOctet = 3 baFirstOct and baSecondOct the user entered values for firstOct and secondOct and baFourthOct should be 255. baThirdOct is determined by the calcValue function. It is the last.broadcastValue. 
	if workingOctet ==3:
		calcValue(3)
		lhFirstOct=firstOct
		lhSecondOct=secondOct
		lhThirdOct=lastBroadcastValue
		lhFourthOct=255
		print "The last host address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "	
	# If workingOctet = 4 baFirstOct, baSecondOct and baThirdOct are all the user entered values for firstOct, secondOct, and thirdOct. baFourthOct is determined by the calcValue function. It is the last.broadcastValue.
	if workingOctet ==4:
		calcValue(4)
		lhFirstOct=firstOct
		lhSecondOct=secondOct
		lhThirdOct=thirdOct
		lhFourthOct=lastBroadcastValue
		print "The broadcast address is "+str(lhFirstOct)+ "."+str(lhSecondOct)+"."+str(lhThirdOct)+"."+str(lhFourthOct)+" "
# Print the Broadcast Address to console. It should be in the form baFirstOct.baSecondOct.baThirdOct.baFourthOct.
broadcastAddress()
'''#--Return the Number of Hosts--#
	# Calculate number of hosts.
		#generate a binaryValue that has 32 characters with the cidrValue determining the number of 1s from left to right.
		#convert the binaryValue to decimal/int form. This is the nuh (number usable hosts) value.
			var nuh = int(binaryValue, 2)
	# Print Number of Usable Hosts (nuh) to console. Should be an int value between 0 and 2,147,483,646. '''