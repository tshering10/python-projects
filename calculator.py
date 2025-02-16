def addition(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def power(num1, num2):
    return num1 ** num2

def calculator():
    history = []
    print("Welcome to the modern Calculator.")
    print("*************************************")
    
    while True:
        print("""
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Power
        6. History
        7. Exit 
        """)
        
        try:
            inputs = int(input("Choose one of the above options (1/2/3/4/5/6): "))
        except ValueError:
            print("Please enter a valid number for the option.")
            continue
        
        if inputs == 7:
            print("Exiting the Calculator. Goodbye!")
            break
        
        if inputs == 6:
            print("Showing calculation history..")
            
            if not history:
                print("No history avalilabe.")
                continue
            for record in history:
                print(record)
                
        if inputs not in [1,2,3,4,5,6]:
            print("Invalid Input. Enter one of the above options. ")
        try:
            num1 = float(input("Enter the first number: "))
        
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        operator = {
            1: addition,
            2: sub,
            3: multi,
            4: div,
            5: power,
            6: history
        }
        
        if inputs in operator:
            result = operator[inputs](num1, num2)
            history_items = f"{num1} {'+' if inputs == 1 else '-' if inputs == 2 else '*' if inputs == 3 else '/' if inputs == 4 else '**'} {num2} = {result}"
            print(f"The result is: {result}")
        else:
            print("Invalid input, please choose a valid operation (1-6).")

        history.append(history_items)
if __name__ == "__main__":
    calculator()
