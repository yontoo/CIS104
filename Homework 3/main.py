import calculator as calc
import msvcrt

fval_str = ""
sval_str = ""
op = ' '
result = 0.0
which_num = 1

print(">")

while(True)
    curr_key = getch()
    if(curr_key == '1' | curr_key == '2' | curr_key == '3' | curr_key == '4' | curr_key == '5' | curr_key == '6'| curr_key == '7' | curr_key == '8' | curr_key == '9' | curr_key == '0'| curr_key == | '.')
        print(curr_key)

        if(which_num == 1)
            fval_str += curr_key
        else
            sval_str =+ curr_key
        break
        


    if(curr_key == 'X' or curr_key == 'x')
        break
