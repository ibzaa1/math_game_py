import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generater_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) +  " "  + operator +  " " +str(right)
    answer = eval(expr)

    return expr, answer

wrong = 0
input("Press Enter to start")
print("----------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generater_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("----------------------------------")
print("Finished in", round(total_time), "seconds")