bot_name:str = "jarvis"
print(f"My name is {bot_name},How can i assist you today?")


while True:
    user_input: str = input("You: ").lower()

    if user_input in ["hey","hi","hello", "hey","hi jarvis","hello jarvis",]:
        print(f"{bot_name}: Hi there! how can i help you today?")

    elif user_input in ["bye","bye jarvis","goodbye","goodbye jarvis"]:
        print(f"{bot_name}: Bye,have a great day!")

    elif user_input in ["+", "add","add two number"]:
        print(f"{bot_name}: sure!let do some addition.Enter two numbers")
        
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            print(f"{bot_name}:The sum of {num1} and {num2} is {num1+num2}")
        except ValueError:
            print(f"{bot_name}:Oops!Please enter a valid number")
            continue
             
    else:
        print(f"{bot_name}: {user_input}? I am not sure I understand. Can you please rephrase?")