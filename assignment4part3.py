#Q.3
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")

