print("Enter 10 values")
value = []
for i in range(10):
    value.append(int(input("Enter value")))
value.sort(reverse=True)
print("The highest value is : ",value[0])

