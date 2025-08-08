from sympy import symbols, Eq, solve, sympify, diff, integrate, sin, cos, tan, cot, sec, csc, simplify, lambdify, limit
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
print("Hello! Welcome to my equation solver.")

while True:
    print("You can solve (equations, differentiation, integration, trig, graphing, goodbye)")
    mode = input().lower()
    if mode == "equations":
        print("Please enter an equation to solve (x only): ")
        userEquation = input()
        splitEq = userEquation.split('=')
        if len(splitEq) > 2:
            print("Please enter the equation in this format (exp. = exp.)")
            exit()
        else:
            #Must convert both exp's into symbolic exp's for combination
            leftSideEq = sympify(splitEq[0])
            rightSideEq = sympify(splitEq[1])
            fullEq = Eq(leftSideEq, rightSideEq)
            soln = solve(fullEq, x)
            print("The answer is: ", soln)
    if mode == "differentiation":
        print("Note, enter higher degree terms like this (ex: 3x^2 is 3*x**2)")
        print("Please enter an expression to differentiate (x only): ")
        diffExpression = input()
        diffExpSym = sympify(diffExpression)
        derivativeSoln = diff(diffExpSym, x)
        print("Derivative of given exp: ", derivativeSoln)
    if mode == "integration":
       print("Definite or indefinite?")
       defOrIndef = input().lower()
       if defOrIndef == "indefinite":
           print("Note, enter higher degree terms like this (ex: 3x^2 is 3*x**2)")
           print("Please enter expression to integrate: ")
           integrateExp = input()
           integrateExpSym = sympify(integrateExp)
           integrateSoln = integrate(integrateExpSym, x)
           print("Indefinite Integral of exp: ", integrateSoln)
       else:
           print("Note, enter higher degree terms like this (ex: 3x^2 is 3*x**2)")
           print("Please enter expression to integrate: ")
           integrateExp = input()
           print("Please enter lower bound: ")
           lB = int(input())
           print("Please enter higher bound: ")
           hB = int(input())
           integrateExpSym = sympify(integrateExp)
           integrateSoln = integrate(integrateExpSym, (x, lB, hB))
           print("Indefinite Integral of exp: ", integrateSoln)
    if mode == "trig":
        print("Note, enter higher degree terms like this (ex: 3x^2 is 3*x**2)")
        print("Please enter a valid trig. equation: ")
        trigExp = input()
        split = trigExp.split('=')
        leftSide = sympify(split[0])
        rightSide = sympify(split[1])
        fullTrig = Eq(leftSide, rightSide)
        soln = solve(fullTrig, x)
        print("Soln: ", soln)
    if mode == "graphing":
        print("Enter an expression to graph (in terms of x): ")
        equation = input()
        SymEquation = sympify(equation)
        #Convert sym equation to numpy for graphing
        toNumpyEq = lambdify(x, SymEquation, modules=['numpy'])
        
        x_range = np.linspace(-10,10,400)
        y_range = toNumpyEq(x_range)
        plt.figure(figsize=(10,5))
        plt.plot(x_range, y_range, label=f"f(x) = {SymEquation}")
        plt.title(f"Graph of: {SymEquation}")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()
    if mode == "goodbye":
        print("Thank you! Have a nice day.")
        exit()
        
    
            
    


