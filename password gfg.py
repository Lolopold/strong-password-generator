import random
list_of_chr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:"
try:
	length_password = int(input("Length of password should be greater be greater than 6:		 "))
	random_password = "".join(random.choices(list_of_chr, k = length_password))
	if length_password > 6:
		print("Your password is: \n"+(random_password))
	else:
		print("password cannot be generated")
except ValueError:
	pass
	print("That wasn't a whole number")
