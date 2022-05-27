def add(a, b):
          return a+ b; 

def sub(a, b):
          return a - b; 

def multiply(a, b):
          return a * b; 

def division(a, b):
          return a / b; 

def modulo(a, b):
          return a % b; 

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Reminder")


while True:
          choice = input("Enter choice(1, 2, 3, 4, 5): ");

          num1 = float(input("Enter the first number: "))
          num2 = float(input("Enter the second number: "))

          if choice in ('1', '2', '3', '4', '5'):

                    if choice == '1':
                              sum = add(num1, num2)

                              print('Result = ' + str(sum))

                    elif choice == '2':
                              subt = sub(num1, num2)
                              print('Result = ' + str(subt))

                    elif choice == '3':
                              multi = multiply(num1, num2)
                              print('Result = ' + str(multi))

                    elif choice == '4':
                              divn = division(num1, num2)
                              print('Result = ' + str(divn))

                    elif choice == '5':
                              modu = modulo(num1, num2)
                              print('Result = ' + str(modu))

                    next_calculation = input("Let's do next calculation? (yes/no): ")

                    if next_calculation == "no" or next_calculation == 'n':
                              break

else: 
          print("Invalid Input")