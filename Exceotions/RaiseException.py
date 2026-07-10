def setAge(age):
    if age < 0:
        raise Exception("age less than 0")
    print(f"Age is set : {age}")


try:
    setAge(-10)

except Exception as e:
    print(e)

else:
    print("lets proceed")
