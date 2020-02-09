import math
def pseudo_linspace(lower, upper, number):
	a=[]
	number=math.floor(number)
	if number==1:
		a.append(round(lower,8))
		return a
	number-=1
	step=(upper-lower)/number
	while round(lower,8)<=upper:
		a.append(round(lower,8))
		lower+=step
	return a



#import math
#def pseudo_linspace(lower, upper, number):
#	a=[]
#	if number==1:
#		a.append(round(lower,8))
#		return a
#	number-=1
#	step=(upper-lower)/number
#	while round(lower,8)<=upper:
#		a.append(round(lower,8))
#		lower+=step
#	return a
#
#lower=float(input("Enter lower bound="))
#upper=float(input("Enter upper bound="))
#number=math.floor(float(input("Enter number of values to be generated=")))
#x=pseudo_linspace(lower, upper, number)
#print(x)
