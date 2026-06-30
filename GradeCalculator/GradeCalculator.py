score = int(input('Enter your grade:'))
try:
	if score >= 90:
		if score >= 96 and score <= 100:
			print('Your grade is A+.')
		elif score >= 92 and score <= 95:
			print('Your grade is A.')					
		else:
			print('Your grade is A-.')

	elif score >= 80:
		if score >= 86 and score <= 89:
			print('Your grade is B+.')
		elif score >= 82 and score <= 85:
			print('Your grade is B.')
		else:
			print('Your grade is B-.')

	elif score >= 70:
		if score >= 76 and score <= 79:
			print('Your grade is C+.')
		elif score >= 72 and score <= 75:
			print('Your grade is C.')
		else:
			print('Your grade is C-.')

	elif score >= 60:
		if score >= 66 and score <= 69:
				print('Your grade is D+.')
		elif score >= 62 and score <= 65:
				print('Your grade is D.')
		else:
			print('Your grade is D-.')
	else:
		print('Your grade is F-.')

except ValueError:
	print("That is an invaid output.")
