#https://stackoverflow.com/questions/46127670/python-3-strange-behavior-of-msvcrt-getch-the-command-used-to-read-individua
#helped me figure out the problem I was having in terms of the interaction between getwch and print. 
import calculator
import msvcrt

expr_done = False
which_num = 1
fval_str = ""
sval_str = ""
print(">", end='', flush = True)
while(True):
    
    #getwch returns keypresses as wide characters in unicode, as opposed to getch wich returns a value in byte format.
    curr_key = msvcrt.getwch()  
    #Tests if curr_key is 0-9 or ".", if it is, print the keypress and add it to fval string or sval string, depending on if the current number being added to is the first or second one.        
    if(curr_key == '1' or curr_key == '2' or curr_key == '3' or curr_key == '4' or curr_key == '5' or curr_key == '6' or curr_key == '7' or curr_key == '8' or curr_key == '9' or curr_key == '0'or curr_key == '.'):
        print(curr_key, end='', flush = True)

        if(which_num == 1 and expr_done):       #Uses the boolean expr_done to determine whether or not the next expression is new, or a continuation of the last result.
            fval_str = ''
            fval_str += curr_key
        elif(which_num == 1):
            fval_str += curr_key
        else:
            sval_str += curr_key
    #Tests if curr_key is "+", "-", "*", "/" or "^". If it is, assign fval to the float of fvla_string and indicate the current number being worked on is the second one.
    #Reset the string values to keep it clean and assign the operation to the keypress.
    if(curr_key == '+' or curr_key == '-' or curr_key == '/' or curr_key == '*' or curr_key == '^'):  
        if (which_num == 1):
            fval = float(fval_str)
            which_num = 2
            fval_str = ""
            sval_str = ""
        op = curr_key
        print(curr_key, end='', flush = True)
    
    #Clears the stored memory when "m" is cleared.
    if(curr_key == 'm' or curr_key == 'M'):
        calculator.clear_mem()
        print("Memory Cleared")
        print(">", end='', flush = True)
    
    #Inverts the current value's sign when "i" is pressed.
    if(curr_key == 'i' or curr_key == 'I'):
        result = calculator.invert(result)
        fval_str = str(result)
        print("Current value inverted. (" + str(result) + ")")
        print(">", end='', flush = True)
    
    #Saves current value in the calculator when "s" is pressed.
    if(curr_key == 's' or curr_key == 'S'):
        calculator.save_mem(result)
        print("Value saved!")
        print(">", end='', flush = True)
    
    #Resets all values in the calculator when "c" is pressed.
    if(curr_key == 'c' or curr_key == 'C'):
        fval = 0.0
        sval = 0.0
        fval_str = ""
        sval_str = ""
        which_num = 1
        result = 0.0
        expr_done = False
        print("Calculator cleared.")
        print(">", end='', flush = True)
        
    #Recalls stored memory when r is pressed.
    if(curr_key == 'r' or curr_key == 'R'):
        result = calculator.call_mem()
        fval_str = str(result)
        print("Stored value is " + str(result) + ".")
        print(">", end='', flush = True)

    #Tests if Enter was pressed. If it was and if sval_string is not empty, choose a function based on the current operator.
    #Also assings the fval_str to the string of result, resets sval_str, sets the current number being worked on to 1 and sets the expr_done indicator to True.
    if(curr_key == chr(13)):
        if (sval_str != ""):
            sval = float(sval_str)
            if (op == '+'):
                result = calculator.add(fval, sval)
                print("\n" + str(result))
                
            elif(op == '-'):
                result = calculator.subtract(fval, sval)
                print("\n" + str(result))
                
            elif(op == '/'):
                result = calculator.divide(fval, sval)
                print("\n" + str(result))
                
            elif(op == '*'):
                result = calculator.multiply(fval, sval)
                print("\n" + str(result))
                
            elif(op == '^'):
                result = calculator.power(fval, sval)
                print("\n" + str(result))
        print(">", end='', flush = True)
        fval_str = str(result)
        sval_str = ""
        which_num = 1
        expr_done = True

              

    #Exits the program when x is pressed.
    if(curr_key == 'X' or curr_key == 'x'):
        break
