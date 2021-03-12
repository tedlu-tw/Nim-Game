print("Please enter how many marbles you would like: ", end = "")
n = int(input())

while n != 0:
	print("Please enter the how many marbles player one is taking: ", end = "")
	take = int(input())
	if n <= 5:
		print("Player one wins!")
		break
	elif take > n or take > 5 or take == 0:
		print("You're entering a number too large.")
	else:
		n -= take
	print("There are", n, "marbles left")
	print("Please enter the how many marbles player two is taking：", end = "")
	take = int(input())
	if n <= 5:
		print("Player two wins!")
		break
	elif take > n or take > 5 or take == 0:
		print("You're entering a number too large")
	else:
		n -= take
	print("There are", n, "marbles left")
