import random
length=int(input("enter the desired length of password: "))
req="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()_-=+/?;:{}[]"
random_password="".join(random.sample(req,length))
print("Your required password is:  ",random_password)
