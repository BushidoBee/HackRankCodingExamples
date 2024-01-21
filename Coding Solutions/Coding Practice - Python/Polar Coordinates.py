# Use 'cmath' module to create the mathematical function
import cmath

# Split the string into three entities; create complex function from values
expression = str(input())
calculations = []
if '+' in expression:
    spl_expr = expression.split('+')
    ipart = spl_expr[1].split('j')
    # Use 'cmath.phase()' function for complex number
    calculations.append(abs(complex(int(spl_expr[0]), int(ipart[0]))))
    calculations.append(cmath.phase(complex(int(spl_expr[0]), int(ipart[0]))))
else:
    if '-' in expression[0]:
        neg_value = expression[0:2]
    spl_expr = expression.split('-')
    ipart = spl_expr[1].split('j')
    calculations.append(abs(complex(int(neg_value), int(ipart[0]))))
    calculations.append(cmath.phase(complex(int(neg_value), int(ipart[0]))))

# Print the result on two lines
print(calculations[0], calculations[1], sep='\n')

# print(*cmath.polar(complex(input())), sep='\n') # Actual Answer
