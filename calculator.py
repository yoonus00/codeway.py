                         #TASK 2 CALCULATOR-CODE WAY INTERNSHIP

def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
   
    print("Welcome to Yoonus's Calculator!")

    while True:
        try:
      
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

    
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = input("Enter choice (1/2/3/4): ")

            if choice not in ('1', '2', '3', '4'):
                print("Invalid choice! Please enter a valid option.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                try:
                    print("Result:", divide(num1, num2))
                except ValueError as ve:
                    print(ve)

            # another calculation
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != 'yes':
                print("Thank you for using yoonus's Calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    calculator()
