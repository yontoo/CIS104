first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
confidence = int(input("What is your confidence in programers between 0 and 100%?: "))
dog_age = age * 7
confidence_deci = float(confidence) / 100

print("Hello, " + first_name + " " + last_name + ", nice to meet you!\nYou might be " + str(age) + " in human years, but in dog years you are " + str(dog_age) + ".")

if confidence_deci < 0.5:
    print("I agree, programmers can't be trusted!")
else:
    print("Writing good code takes hard work.")