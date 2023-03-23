import random
def primeCheck(num):
	if num < 2:
		return False
	elif num in {2,3}:
		return True
	elif num % 2 == 0:
		return False
	else:
		for i in range(3,num-1,2):
			if num % i == 0: 
				return False
		else:
			return True
#end primeCheck
def pretAvg(num,sub1=3,cont=True):
	sample = num
	sample *=2
	while cont:
		if primeCheck(sub1):
			if primeCheck(sample-sub1):
				sub2 = sample-sub1
				cont = False
			#end if
			else:
				sub1+=1   
		else:
			sub1+=1
		#end if   
	#end while  
	return sub1,sub2
#end pretAvg

limit = int(input('How many numbers do you want? '))
nList = [random.randrange(4,20) for i in range(limit)]
print("Your numbers are:", nList)
for i in nList:
  num1 = pretAvg(i)[0]
  num2 = pretAvg(i)[1]
  print("The two prime numbers whose average is %d are %d and %d."%(i, num1, num2))