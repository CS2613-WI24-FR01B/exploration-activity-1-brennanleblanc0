from sympy import *

t, T, n, A = symbols('t T n A')
init_printing(use_unicode=True)

print("Signal Proccessor (for periodic signals)")
command : str = ' '
period : float = 0.0
amplitude : float = 0.0
while(command != 'X'):
    command = input("Enter f(t) or X to quit: ")
    if (command.upper() == "X"):
        break
    f_t = sympify(command)
    aVal = input("Enter a value for A (0 if none is needed): ")
    tVal = input("Enter a value for T: ")
    a_zer = integrate((1/T) * f_t, (t, 0, T))
    a_n = integrate((2/T) * f_t * cos(2*pi*n*t/T), (t, 0, T))
    b_n = integrate((2/T) * f_t * sin(2*pi*n*t/T), (t, 0, T))
    print("The expression for a_0: ", a_zer.subs(A, aVal).subs(T, tVal))
    print("The value for a_0: ", a_zer.subs(A, aVal).subs(T, tVal).evalf())
    for i in range(1,6):
        print("The expression for a_", i, ": ", a_n.subs(n, i).subs(A, aVal).subs(T, tVal))
        print("The value for a_", i, a_n.subs(n, i).subs(A, aVal).subs(T, tVal).evalf())
    for i in range(1,6):
        print("The expression for b_", i, ": ", b_n.subs(n, i).subs(A, aVal).subs(T, tVal))
        print("The value for b_", i, b_n.subs(n, i).subs(A, aVal).subs(T, tVal).evalf())
    
    
