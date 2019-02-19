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
    
    curr_key = msvcrt.getwch()
    if(curr_key == '1' or curr_key == '2' or curr_key == '3' or curr_key == '4' or curr_key == '5' or curr_key == '6' or curr_key == '7' or curr_key == '8' or curr_key == '9' or curr_key == '0'or curr_key == '.'):
        print(curr_key, end='', flush = True)

        if(which_num == 1 and expr_done):
            fval_str = ''
            fval_str += curr_key
        elif(which_num == 1):
            fval_str += curr_key
        else:
            sval_str += curr_key

    if(curr_key == '+' or curr_key == '-' or curr_key == '/' or curr_key == '*' or curr_key == '^'):  
        if (which_num == 1):
            fval = float(fval_str)
            which_num = 2
            fval_str = ""
            sval_str = ""
        op = curr_key
        print(curr_key, end='', flush = True)
    
    if(curr_key == 'm' or curr_key == 'M'):
        calculator.clear_mem()
        print("Memory Cleared")
    
    if(curr_key == 'i' or curr_key == 'I'):
        result = calculator.invert(result)
        fval_str = str(result)
        print("Current value inverted. (" + str(result) + ")")
    
    if(curr_key == 's' or curr_key == 'S'):
        calculator.save_mem(result)
        print("Value saved!")
    
    if(curr_key == 'c' or curr_key == 'C'):
        fval = 0.0
        sval = 0.0
        fval_str = ""
        sval_str = ""
        which_num = 1
        result = 0.0
        print("Calculator cleared.")
        

    if(curr_key == 'r' or curr_key == 'R'):
        result = calculator.call_mem()
        fval_str = str(result)
        print("Stored value is " + str(result) + ".")

        
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

              


    if(curr_key == 'X' or curr_key == 'x'):
        break
