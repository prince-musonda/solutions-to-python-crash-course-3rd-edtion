prompt = '\nTell you age and i will info you the price for movie ticket based on your age?'
prompt += '\nEnter "quit" to quit: '

while True:
	age = input(prompt)

	if age == 'quit':
		break
	else:
		age = int(age)

		if age < 3:
			price = 0
		elif age <= 12:
			price = 10
		else:
			price = 15

	print(f'Movie ticket price: $ {price}')
