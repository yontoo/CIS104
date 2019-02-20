import math

current_mem = 0.0

def add(n1, n2):
    return n1 + n2

def  subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

#Function to divide 2 inputed numbers.
def divide(n1, n2):
    return n1 / n2

#Function to get the result of n1 to the power of n2.
def power(n1, n2):
    return math.pow(n1, n2)

#Inverts the inputed number.
def invert(n1):
    return n1 * -1

#Returns the value in the varialbe current_mem
def  call_mem():
    return current_mem

#Assigns the global variable current_mem to the inputed number.
def save_mem(n1):
    global current_mem
    current_mem = n1

#Assigns the global variable current_mem to 0.
def clear_mem():
    global current_mem
    current_mem = 0.0