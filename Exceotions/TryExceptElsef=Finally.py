
try:
    number = int(input("Enter a number"))
    result = 100 / number

except ZeroDivisionError:
      print("cant divide number by zero")

except ValueError:
    print("Value error occured")

except :
    print("Something went wrong")

else:
     print(f"Result is{result}")

finally:

     print("Execution completed")

