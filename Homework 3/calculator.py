import math

current_mem = 0.0

def add(n1, n2):
    return n1 + n2

def  subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return math.pow(n1, n2)

def invert(n1):
    return n1 * -1

def  call_mem():
    return current_mem

def save_mem(n1):
    global current_mem
    current_mem = n1

def clear_mem():
    global current_mem
    current_mem = 0.0