def int_division(dividend, divisor):
    try:
        print(int(dividend) // int(divisor))
        
    except ValueError as v_err:
        print ("Error Code:", v_err)
        
    except ZeroDivisionError as z_err:
        print ("Error Code:", z_err)

t_cases = int(input())
    
for test in range(t_cases):
    case = input().split()
    int_division(case[0], case[1])
