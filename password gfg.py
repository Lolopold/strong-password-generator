import random
list_of_chr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:"
length_password = int(input("Length of password should be greater be greater than 6:		 "))
random_password = "".join(random.sample(list_of_chr,k = length_password))
if length_password > 6:
	print(f"Your password is \n{random_password}")
else:
	print("password cannot be generated")
