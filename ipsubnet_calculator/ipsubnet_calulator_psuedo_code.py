# Calculator for CIDR based IP Subnetting
# Returns the Network Mask, Network Address, First Host Address, Last host Address, Broadcast Address, Number of Hosts. Each is in dot decimal form. Values can be anywhere from 0.0.0.0 through 255.255.255.255.

#---------- BEGIN CODE ----------#
#User Input
	#Get User to type in the IP address divided by octets -- firstOct, secondOct, thirdOct, fourthOct- and CIDR slash-value - cidrValue.
# Return Network Mask
	#Convert CIDR notation to dot decimal netmask. This returns the Network Mask.
	# ADD CALC HERE
	# Print the Network Mask to console.
# Return the Network Address
	# Get the multiplication/division factor -mdf- ( can be 128,64,32,16,8,2 or 1) and the octet value (can be 1-3) based on the CIDR value .
		# If the cidrValue is < 8 then the mdf options are 128,64,32,16,8,2 and 1  in descending order. We are in working the first octet. octetValue=0 
		# If the cidrValue is greater than 8 
			#To get the octetValue take the whole # part of the cidrValue/8. Each full whole number (1,2 etc.) represents a full octet so octetValue=1 is 255.x.x.x  working in the 2nd octet. If octetValue is 2 we are working in the 3rd octet which is 255.255 etc. 
				# The workingOctet value is n+1 where n is the whole # (int) part of the cidrValue/8
			# Then to get the mdf take the cidrValue%8 (remainder) and the number should be an int value between 1-7 which corresponds to mdf options are 128,64,32,16,8,2 and 1 descending.
	# Define the calcValue function.
		# First the workingOctet number cooresponds to the firstOct, secondOct, thirdOct and fourthOct respectively. That user entered value then becomes the startNumber.
		# divide the startNumber by the mdf. Take the int of this value (we only want the whole number part) this becomes the wnValue (stands for whole number value).
		# multiply the wnValue by the mdf.  This value is becomes net.firstValue.
		# multiply (wnValue+1) by the mdf. Then -1 from that value.  This becomes the last.broadcastValue.
	# Create cases based on the workingOctet value. naXOct stands for network address (ordinal number) Octet. 
		# If workingOctet = 1 naSecondOct, naThirdOct,and naFourthOct should be 0. naFirstOct is determined by the calcValue function. It is the net.firstValue. 
		# If workingOctet = 2 naFirstOct should be 255 while naThirdOct and naFourthOct should be 0. naSecondOct is determined by the calcValue function . It is the net.firstValue. 
		# If workingOctet = 3 naFirstOct and naSecondOct should be 255 while naFourthOct should be 0. naThirdOct is determined by the calcValue function. It is the net.firstValue. 
		# If workingOctet = 4 naFirstOct, naSecondOct and naThirdOct are all 255. naFourthOct is determined by the calcValue function. It is the net.firstValue. 
	# Print the Network Address to console. It should be in the form naFirstOct.naSecondOct.naThirdOct.naFourthOct.
# Return the First Host Address
	# Create cases based on the workingOctet value. fhXOct stands for first host (ordinal number) Octet. 
		# If workingOctet = 1 fhSecondOct, fhThirdOct,and fhFourthOct should be 0 should be 1. fhFirstOct is determined by the calcValue function. It is the net.firstValue. 
		# If workingOctet = 2 fhFirstOct should be 255 while fhThirdOct should be 0 and fhFourthOct should be 1. fhSecondOct is determined by the calcValue function . It is the net.firstValue. 
		# If workingOctet = 3 fhFirstOct and fhSecondOct should be 255 while fhFourthOct should be 1. fhThirdOct is determined by the calcValue function. It is the net.firstValue. 
		# If workingOctet = 4 fhFirstOct, fhSecondOct and fhThirdOct are all 255. fhFourthOct is determined by the calcValue function. (It is the net.firstValue+1)
	# Print the First Host Address to console. It should be in the form fhFirstOct.fhSecondOct.fhThirdOct.fhFourthOct.
# Return the Last host Address
	# Create cases based on the workingOctet value. lhXOct stands for last host (ordinal number) Octet. 
		# If workingOctet = 1 lhSecondOct, lhThirdOct,should be 255 lhFourthOct should be 254. lhFirstOct is determined by the calcValue function. It is the last.broadcastValue. 
		# If workingOctet = 2 lhFirstOct and  lhThirdOct should be 255 and lhFourthOct should be 254. lhSecondOct is determined by the calcValue function . It is the last.broadcastValue.  
		# If workingOctet = 3 lhFirstOct and lhSecondOct should be 255 while lhFourthOct should be 254. lhThirdOct is determined by the calcValue function. It is the last.broadcastValue. 
		# If workingOctet = 4 lhFirstOct, lhSecondOct and lhThirdOct are all 255. lhFourthOct is determined by the calcValue function. It is the last.broadcastValue.-1
	# Print the Last host Address to console. It should be in the form lhFirstOct.lhSecondOct.lhThirdOct.lhFourthOct.
# Return the Broadcast Address
	# Create cases based on the workingOctet value. baXOct stands for broadcast address (ordinal number) Octet. 
		# If workingOctet = 1 baSecondOct, baThirdOct and baFourthOct should be 255. baFirstOct is determined by the calcValue function. It is the last.broadcastValue. 
		# If workingOctet = 2 baFirstOct and  baThirdOct and baFourthOct should be 255. baSecondOct is determined by the calcValue function . It is the last.broadcastValue.  
		# If workingOctet = 3 baFirstOct and baSecondOct and baFourthOct should be 255. baThirdOct is determined by the calcValue function. It is the last.broadcastValue. 
		# If workingOctet = 4 baFirstOct, baSecondOct and baThirdOct are all 255. baFourthOct is determined by the calcValue function. It is the last.broadcastValue.
	# Print the Broadcast Address to console. It should be in the form baFirstOct.baSecondOct.baThirdOct.baFourthOct.
# Return the Number of Hosts
	# Calculate number of hosts.
		#generate a binaryValue that has 32 characters with the cidrValue determining the number of 1s from left to right.
		#convert the binaryValue to decimal/int form. This is the nuh (number usable hosts) value.
			var nuh = int(binaryValue, 2)
	# Print Number of Usable Hosts (nuh) to console. Should be an int value between 0 and 2,147,483,646. 