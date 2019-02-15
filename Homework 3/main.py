import calculator
import msvcrt

result = 0.0


def main():
    fval = 0
    sval = 0
    fval_str = ""
    sval_str = ""
    op = ' '

    which_num = 1
    curr_key = ''
    print(">")
    while(True):
        curr_key = msvcrt.getch()
        if(curr_key == '1' or curr_key == '2' or curr_key == '3' or curr_key == '4' or curr_key == '5' or curr_key == '6' or curr_key == '7' or curr_key == '8' or curr_key == '9' or curr_key == '0'or curr_key == '.'):
            print(curr_key)

            if(which_num == 1):
                fval_str += curr_key
            else:
                sval_str += curr_key
            break
        if(curr_key == '+' or curr_key == '-' or curr_key == '/' or curr_key == '*' or curr_key == '^'):  
            if (which_num == 1):
                fval = float(fval_str)
                which_num = 2
                fval_str = ""
                sval_str = ""
            op = curr_key
            print(curr_key)
            break
        if(curr_key == chr(13)):
            print("\n")
            if (sval_str != ""):
                sval = float(sval_str)
                if (op == '+'):
                    global result
                    result = calculator.add(fval, sval)
                    break
                elif(op == '-'):
                    result = calculator.subtract(fval, sval)
                    break
                elif(op == '/'):
                    result = calculator.divide(fval, sval)
                    break
                elif(op == '*'):
                    result = calculator.multiply(fval, sval)
                    break
                elif(op == '^'):
                    result = calculator.power(fval, sval)
                    break


        if(curr_key == 'X' or curr_key == 'x'):
            break
