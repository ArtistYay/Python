import re
def arithmetic_arranger(problems, solve = False):
    if(len(problems) > 5):
      return "Error: Too many problems."


    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      n = problem.split(" ")
      num1 = n[0]
      operator = n[1]
      num2 = n[2]

      if(len(num1) >= 5 or len(num2) >= 5): 
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if(operator == "+"):
        sum = str(int(num1) + int(num2))
      elif(operator == "-"): 
        sum = str(int(num1) - int(num2))

      length = max(len(num1), len(num2)) + 2
      top = str(num1).rjust(length)
      bottom = operator + str(num2).rjust(length - 1)
      line = ""
      res = str(sum).rjust(length)
      for s in range(length):
        line += "-"

      if problem != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else: 
        first += top
        second += bottom
        lines += line
        sumx += res 

    if solve: 
      string = first + "\n" + second + "\n" + lines + "\n" + sumx 
    else: 
      string = first + "\n" + second + "\n" + lines 
    return string
