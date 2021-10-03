
import random
passlen = int(input("enter the length of password: "))
letters="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwd = "".join(random.sample(letters,passlen ))
print(passwd)
