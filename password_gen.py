import string
import random
print()

print("Welcome To Password Genetor Format")

print()

Enter = int(input("Please Enter How Many Length Password You Need :"))
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

combine = s1 + s2 + s3 + s4


d = random.sample(combine,Enter)

Password = "".join(d)
print()

print("Your Generated Password Is :",Password)
print()




    



