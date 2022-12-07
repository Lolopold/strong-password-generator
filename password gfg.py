import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:"
if length_password = int(input("length should be greater be greater than 6 "))
        print("Enter the length of the password")
else:
    print("password csnnot be generated")
a = "".join(random.sample(password,length_password))
print(f"Your password is {a}")
