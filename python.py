def add_two_numbers():
    while True:
        try:
            # Read first integer
            num1 = int(input("Enter first integer: "))
            
            # Read second integer
            num2 = int(input("Enter second integer: "))
            
            # Calculate sum
            total = num1 + num2
            
            # Display result
            print(f"Sum of {num1} and {num2} is: {total}")
            break  # Exit loop after successful input
        
        except ValueError:
            print("Invalid input. Please enter integers only.")

# Run the function
if __name__ == "__main__":
    add_two_numbers()
