# Mark Lorenz P. Natividad
# ICT-105

try:
	birthday = int(input("Enter your Birth day: "))
	birthmonth = int(input("Enter your Birth month: "))

	match birthmonth:
		case 1:
			if 1 <= birthday <= 19:
				print("Your zodiac sign is Capricorn.")
			elif 20 <= birthday <= 31:
				print("Your zodiac sign is Aquarius.")
			else:
				print("Invalid Input.")
		case 2:
			if 1 <= birthday <= 18:
				print("Your zodiac sign is Aaquarius.")
			elif 19 <= birthday <= 28:
				print("Your zodiac sign is Pisces.")
			else:
				print("Invalid Input.")
		case 3:
			if 1 <= birthday <= 20:
				print("Your zodiac sign is Pisces.")
			elif 20 <= birthday <= 28:
				print("Your zodiac sign is Aries.")
			else:
				print("Invalid Input.")
		case 4:
			if 1 <= birthday <= 19:
				print("Your zodiac sign is Aries.")
			elif 20 <= birthday <= 28:
				print("Your zodiac sign is Taurus.")
			else:
				print("Invalid Input.")
		case 5:
			if 1 <= birthday <= 20:
				print("Your zodiac sign is Taurus.")
			elif 21 <= birthday <= 31:
				print("Your zodiac sign is Gemini.")
			else:
				print("Invalid Input.")
		case 6:
			if 1 <= birthday <= 21:
				print("Your zodiac sign is Gemeni.")
			elif 22 <= birthday <= 30:
				print("Your zodiac sign is Cancer.")
			else:
				print("Invalid Input.")
		case 7:
			if 1 <= birthday <= 22:
				print("Your zodiac sign is Cancer.")
			elif 23 <= birthday <= 31:
				print("Your zodiac sign is Leo.")
			else:
				print("Invalid Input.")
		case 8:
			if 1 <= birthday <= 22:
				print("Your zodiac sign is Leo.")
			elif 23 <= birthday <= 31:
				print("Your zodiac sign is Virgo.")
			else:
				print("Invalid Input.")
		case 9:
			if 1 <= birthday <= 21:
				print("Your zodiac sign is Scorpio.")
			elif 22 <= birthday <= 30:
				print("Your zodiac sign is Sagittarius.")



except ValueError:
	print ("Invalid input. Please enter an integer.")

except Exception as e:
	print (f"An unexpected error occured: {e}")

finally:
	print ("Execution complete.")
















