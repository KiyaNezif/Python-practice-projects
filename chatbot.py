bot_name: str = "Bob"
print(f"Hello! I am {bot_name}. How can I assist you today?")

while True:
    #turns all user input to lowercase to make it easier to compare
    user_input= input("You: ").lower()

    if user_input in ["hi","hallo", "hello","hei"]:
        print(f"{bot_name}: Hello! How can I help you?")
    elif user_input in['bye', 'goodbye']:
        print(f"{bot_name}: Goodbye! Have a great day!")
    elif user_input in ['+', '-', '*', '/']:
        print(f"{bot_name}: I can help you with that! Please enter the numbers and the operator.")
        try: 
            num1: float = float(input("Enter the first number: "))
            num2: float = float(input("Enter the second number: "))
            operator: str = input("Enter an operator (+, -, *, /): ")
            print(f"{bot_name}: The result is: {eval(f'{num1} {operator} {num2}')}")
        except Exception as e:
            print(f"{bot_name}: Sorry, I couldn't perform the calculation. Please make sure to enter valid numbers and operators.")

        else:
            print(f"{bot_name}: I'm sorry, I don't understand that. Can you please rephrase?")
        break