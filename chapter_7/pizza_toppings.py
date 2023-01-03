prompt = '\nwhen you are done, enter the word "quit".\n'
prompt += 'Enter the toppping that you want us to add to you pizza: '


while True:
	requested_topping = input(prompt)
	if requested_topping.lower() == 'quit':
		break
	else:
		print(f'okay, we will add {requested_topping} to your pizza')