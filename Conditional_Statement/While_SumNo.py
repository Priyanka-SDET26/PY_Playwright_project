
Num = int(input("Enter a Number: "))

temp = 0

while Num > 0:
    Digit = Num %10
    temp = temp+Digit
    Num = Num//10


print("Sum of num :",temp)

