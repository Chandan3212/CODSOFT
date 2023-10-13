num1=float(input("enter number 1: "))
num2=float(input("enter number 2: "))
print("enter + for addition\nenter - for subtraction\nenter* for multiplication\nenter / for division\nenter ** for exponintioal\nenter // for floor division\n")
choice=input("enter your choice")
if(choice=="+"):
    print("sum of ",num1,"and",num2,"is",num1+num2)
elif(choice=="-"):
    print("Differecne of",num1,"and",num2,"is",num1-num2)
elif(choice=="*"):
    print("Product of ",num1,"and",num2,"is",num1*num2)
elif(choice=="/"):
    print("Division of ",num1,"and",num2,"is",num1/num2)
elif(choice=="**"):
    print("Power of",num1,"^",num2,"is",num1**num2)
elif(choice=="//"):
    print("Float division of",num1,"and",num2,"is",num1//num2)
