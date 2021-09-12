## Made by Kai De Xie

def sort_gcd_calculations(first_integer,second_integer):
  '''
  Given first_integer and second_integer, returns main_gcd_calculator where
  first_integer is the greater of the two inital given integers and 
  second_integer is smaller. 
  '''
  if second_integer > first_integer:
    return main_gcd_calculator(second_integer,first_integer)
  else:
    return main_gcd_calculator(first_integer,second_integer)
  
def main_gcd_calculator(first_integer,second_integer):
  '''
  Given two non-zero integers, first_integer and second_integer, with 
  first_integer greater or equal to second_integer, finds the 
  Greatest Common Divisor between the two integers using Euclidean Algorithm
  '''
  next_second_integer = first_integer % second_integer
  if next_second_integer == 0:
    print(second_integer)
    return second_integer
  else:
    return main_gcd_calculator(second_integer,next_second_integer)

def gcd_calculator():
  '''
  Requests Users for two non-zero integers. Finds the Greatest Common Divisor 
  between the two integers using Euclidean Algorithm
  '''
  first_integer = ""
  while (not(first_integer.isnumeric()) or (first_integer == "0")):
    first_integer = input("Do not add spaces. Enter first desired integer:")
    if first_integer[0] == "-":
      first_integer = first_integer[1:]
    if (not(first_integer.isnumeric()) or (first_integer == "0")):
      print("Input must be non-zero integer. Try Again")
  second_integer = ""
  while (not(second_integer.isnumeric()) or (second_integer == "0")):
    second_integer = input("Do not add spaces. Enter second desired integer:")
    if second_integer[0] == "-":
      second_integer = second_integer[1:]
    if (not(second_integer.isnumeric()) or (second_integer == "0")):
      print("Input must be non-zero integer. Try Again")
  first_integer = int(first_integer)
  second_integer = int(second_integer)
  return sort_gcd_calculations(first_integer,second_integer)