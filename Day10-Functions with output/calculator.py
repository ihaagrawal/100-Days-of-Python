#calculator
#add
def add(n1, n2):
  return n1+n2

#subtract
def sub(n1, n2):
  return n1 - n2

#multiply
def multi(n1, n2):
  return n1*n2

#divide
def div(n1, n2):
  return n1/n2

operations = {
  "+":add, 
  "-":sub, 
  "*":multi, 
  "/":div
}

def calculator():

  num1 = float(input("First Number: "))
  num2 = float(input("Second Number: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    op_sym = input("Select Operation: ")
    
    should_continue = True
    
    calc = operations[op_sym]
    answer = calc(num1, num2)
    
    print(f"{num1} {op_sym} {num2} = {answer}")
  
    if input("Continue? y or n: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()