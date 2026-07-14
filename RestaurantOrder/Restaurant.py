#Mark Lorenz P. Natividad
#ICT-105

Menu_Prices = []


def Title():
	print("---------Jolly McYummy---------")
	print("[1] Meals\n[2] Pasta\n[3] Burger\n[4] Dessert\n[5] Drinks\n[0] Exit")


def meals():
	global Menu_Prices
	print("---------Meals---------")
	meals_menu = ["[A] 1 Piece ChickenManok with Kanin", "[B] 2 Pieces ChickenManok with Kanin",
				  "[C] 3 Pieces BurgirStik with BFF Fries Premium", "[D] 1 Piece BurgirStik with Kanin"]
	meals_prices = [99, 180, 169, 67]
	Menu_Prices.extend(meals_prices)
	for meal in meals_menu:
		print(meal)


def pasta():
	global Menu_Prices
	print("---------Pasta---------")
	pasta_menu = ["[A] Solo YummyCarbonara", "[B] Solo Yummyghetti", "[C] Anita Max Wynn Palabok", "[D] Cheesy Macaroro"]
	pasta_prices = [76, 89, 70, 90]
	Menu_Prices.extend(pasta_prices)
	for pasta in pasta_menu:
		print(pasta)


def burger():
	global Menu_Prices

	print("---------Burger---------")
	burger_menu = ["[A] 1 piece Solo Original YumBurgir", "[B] 1 piece Sigma Burgir", "[C] 1 piece Special Chili cheese Burgir",
				   "[D] Jolly McYummy Burgir Overload"]
	burger_prices = [60, 80, 110, 150]
	Menu_Prices.extend(burger_prices)
	for burger in burger_menu:
		print(burger)


def dessert():
	global Menu_Prices
	print("---------Dessert---------")
	dessert_menu = ["[A] Vanilla Monday Ice Cream", "[B] Chocolate Monday Ice Cream", "[C] 10 pieces Banana Cute",
					"[D] Peach Mango Cutie Pie ", "[E]Jolly Yummy ChocoMallows Cutie Pie"]
	dessert_prices = [50, 60, 70, 40, 49]
	Menu_Prices.extend(dessert_prices)
	for dessert in dessert_menu:
		print(dessert)


def drinks():
	global Menu_Prices
	print("---------Drinks---------")
	drinks_menu = ["[A] Regular Cocacolastic (coke) ", "[B] Regular Fantastic (fanta) l", "[C] iShowSpritSprit (sprite)", "[D]Unlimited C2 na kulay Green Premium"]
	drinks_prices = [30, 35, 30, 90]
	Menu_Prices.extend(drinks_prices)
	for drink in drinks_menu:
		print(drink)


def calculate_order():
	global Menu_Prices
	global user_choice

	order_quantity = int(input("Quantity?: "))
	total_price = Menu_Prices[user_choice] * order_quantity
	print(f"Your order total is: {total_price:,.2f}")
	user_cash = int(input("Amount Tendered: "))
	user_change = user_cash - total_price

	if user_change >= 0:
		print(f"Your change is Php{user_change:,.2f}")
	else:
		print("Not enough cash. Try again.")


retry = -99

# int main(){

while True:
	Title()
	try:
		user_menu = int(input("CHOICE: "))

	except ValueError:
		print("Invalid Input.")

	match (user_menu):
		case 0:  # Exit
			print("Thank you for visiting Jolly McYummy")
			break
		case 1:  # Meals
			while True:
				meals()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 2:  # pasta
			while True:
				pasta()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99
				except ValueError:
					print("Invalid Choice")
		case 3:  # burger
			while True:
				burger()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 4:  # dessert
			while True:
				dessert()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
						case 'E':
							user_choice = 4
							calculate_order()

					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 5:  # drinks
			while True:
				drinks()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")











