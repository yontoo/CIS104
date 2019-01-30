age = int(input("Enter your age: "))
older_age = age + 10
temp = float(input("Enter the temperature in Fahrenheit: "))
temp_c = (temp - 32) * 5 / 9

print("In 10 years you will be " + str(older_age) + ".\n" + str(temp) + " degrees Fahrenheit is " + str(temp_c) + " degrees in Celsius.")