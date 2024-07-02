from ast import expr
import random
import time

operators =["+","-","*"]
Min_operand=3
Max_operand=12
Total_problems= 5

def generate_problem():
  left = random.randint(Min_operand, Max_operand)
  right= random.randint(Min_operand,Max_operand)

  operator =random.choice(operators)

  expr= str(left) + "" + operator + "" + str(right)
  answer= eval(expr)
  return expr,answer
  

wrong = 0
name= input("Please enter your name:")
input("Press enter to start!!")
print("Ready. Set. Goo.!")

start_time = time.time()

for i in range(Total_problems):
  expr,answer=generate_problem()
  while True:
      guess= input("Problem #" +str(i+1)+ ":"+ expr+"=")
      if guess == str(answer):
        break
      wrong += 1

end_time = time.time()
total_time= end_time - start_time


print("Thank you for Playing")
print("Great work, Well done", name, "You finished in:", total_time, "seconds!!" )
