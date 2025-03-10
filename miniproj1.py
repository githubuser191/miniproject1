def calculator():
  while True:
    print("Available Operation:")
    operation={
        1:"Addition",
        2:"Subtraction",
        3:"Multiplication",
        4:"Division",
        5:"Modulus",
        6:"Percentage",  
        7:"Square"       
    }
    print(operation)
    def add(a,b):
      return a+b
    def sub(a,b):
      return a-b
    def mul(a,b):
      return a*b
    def divide(a,b):
        try:
         return a/b
        except ZeroDivisionError:
          return "Error: Division by zero is not allowed."
    def mod(a,b):
      return a%b
    def square(c):
        return c**2
    def percent(a,b):
      try:
       return (a/b)*100
      except ZeroDivisionError:
        return "Error: Total marks cannot be zero."
    try:
      w=int(input("Enter Your Choice 1 to 7:"))
      if w in [1,2,3,4,5]:
        a=int(input("Enter First Number: "))
        b=int(input("Enter Second Number: "))
      elif(w==6):
        a=int(input("Enter Obtained Marks:"))
        b=int(input("Enter Total Marks:")) 
      elif(w==7):
        c=int(input("Enter a Number:"))   
      match w:
        case 1:
          print(f'The sum of {a} and {b} =', add(a,b))    
        case 2:
          print(f'The subtraction of {a} and {b} =', sub(a,b))  
        case 3:
          print(f'The multiplication of {a} and {b} =', mul(a,b))     
        case 4:
          print(f'The division of {a} and {b} =', divide(a,b)) 
        case 5:
          print(f'The modulus of {a} and {b} =', mod(a,b)) 
          
        case 6:
          print(f'Percentage =', percent(a,b))
        case 7:
          print(f'The square of {c}  =', square(c)) 
        case _:
          print("Enter a choice from 1 to 7")
    except ValueError:
        print("Error: Please enter a valid number.")
calculator()
