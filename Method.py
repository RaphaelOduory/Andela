def prime_number(num):
	for num in range(2, num):
		Prime = True
		for i in range(2,num):
				if (num%i) == 0:
					Prime = False
		if Prime:
				print(num)
prime_number(11)
