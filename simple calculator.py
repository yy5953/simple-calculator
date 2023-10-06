def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  return x/y

print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.divide")

while True :
  option = input("enter your option(1/2/3/4):")

  if option in ('1', '2', '3', '4'):
    try:
      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))
    except ValueError:
         print("Invalid input. Please enter a number.")
         continue

    if  option == '1':
         print(num1, "+", num2, "=", add(num1, num2))

    elif option == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif option == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

    elif option == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
      break
  else:
    print("Invalid Input")