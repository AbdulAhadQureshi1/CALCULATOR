import math
def three_num():
    print('''
    INPUT FORMAT: 
            first number space operator space second number space operator space third number
    ''')
    a,o,b,o2,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    o = o.lower()
    o2 = o.lower()
    return a,b,c,o,o2
def two_num():
    print('''
    INPUT FORMAT:
            first number space operator space second number
    ''')
    a,o,b = input().split()
    a = int(a)
    b = int(b)
    o = o.lower()
    return a,b,o
def trignometric():
    func, angle = input().split()
    angle = float(angle)
    angle = angle * (math.pi/180)
    func = func.lower()
    return func, angle
def logarithmic():
    func, number, base = input().split()
    number = float(number)
    base = base.lower()
    func = func.lower()
    return func, number, base
#----------------------------------------------------------------------------------------------------MAIN PROGRAM-----------------------------------------------------------------------------------------------------
flag = True
while flag:
    print('''
    ==============================================================================================WELCOME TO ABDUL AHAD's CALCULATOR=======================================================================================
    ==>> CHOOSE WHAT YOU WANT TO CALCULATE:
    1. \t SIMPLE ARITHMETIC B/W 2 OR 3 NUMBERS
    2. \t LOGARITHMIC FUNCTIONS
    3. \t TRIGNOMETRIC FUNCTIONS
    4. \t DERIVATIVE OF PLOYNOMIAL
    ''')
    choice = int(input("\n Your choice from above four: \t "))
    if choice == 1:
        print('''
        ===============================================================================================ARITHMETIC CALCULATOR================================================================================================
        1. \t BETWEEN 2 NUMBERS
        2. \t BETWEEN 3 NUMBERS

        ''')
        choice2 = int(input())
        print('''
        ==>> NOTE:
                x -> Multiplication
                / -> Division (1st/2nd)
                + -> Addition
                - -> Subtraction (1st-2nd)
                ^ -> Power (1st power 2nd)

        ''')
        if choice2 == 2:
            a,b,c,o,o2 = three_num()
            if o == '+':
                if o2 == '-':
                    print("Output : \t", a + b - c)
                elif o2 == '+':
                    print("Output: \t", a + b + c)
                elif o2 == '/':
                    print("Output: \t", a + b / c)
                elif o2 == 'x':
                    print("Output: \t", a + b * c)
            elif o == '-':
                if o2 == '-':
                    print("Output : \t", a - b - c)
                elif o2 == '+':
                    print("Output: \t", a - b + c)
                elif o2 == '/':
                    print("Output: \t", a - b / c)
                elif o2 == 'x':
                    print("Output: \t", a - b * c)
            elif o == 'x':
                if o2 == '-':
                    print("Output : \t", a * b-c)
                elif o2 == '+':
                    print("Output: \t", a * b+c)
                elif o2 == '/':
                    print("Output: \t", a * b / c)
                elif o2 == 'x':
                    print("Output: \t", a * b * c)
            elif o == '/':
                if o2 == '-':
                    print("Output : \t", a / b-c)
                elif o2 == '+':
                    print("Output: \t", a / b+c)
                elif o2 == '/':
                    print("Output: \t", a / b / c)
                elif o2 == 'x':
                    print("Output: \t", a / b * c)
        elif choice2 == 1:
            a,b,o = two_num()
            if o == '+':
                print("Output: \t ", a + b)
            elif o == '-':
                print("Output: \t ", a - b)
            elif o == 'x':
                print("Output: \t ", a * b)
            elif o == '/':
                print("Output: \t ", a / b)
            elif o == '^':
                print("Output: \t ", a ** b)
    if choice == 2:
        print('''
        ==============================================================================================LOGARITHMIC CALCULATOR===========================================================================================
        ==>> INPUT FORMAT:
                        log space number space base
        
        ''')
        func, number, base = logarithmic()
        if base == 'e':
            print("Output: \t ", math.log(number, math.e))
        elif base == 10:
            base = float(base)
            print("Output: \t ", math.log10(number))
        else:
            base = float(base)
            print("Output: \t ", math.log(number, base))
    if choice == 3:
        print('''
        ================================================================================================TRIGNOMETRIC CALCULATOR========================================================================================
        ==>> INPUT FORMAT:
                    function(sin, cos, tan, sinh, cosh, tanh etc.) space angle(in degrees)
        ==>> FUNCTIONS : 
                    sin, cos, tan, cosec, sec, cot, sinh, cosh, tanh, coth, cosech, sech
        ''')
        while True:
            func, angle = trignometric()
            if func == "sin":
                print("Output: \t ", math.sin(angle))
                break
            elif func == "cos":
                print("Output: \t ", math.cos(angle))
                break
            elif func == "tan":
                print("Output: \t ", math.tan(angle))
                break
            elif func == "cot":
                print("Output: \t ", 1/math.tan(angle))
            elif func == "cosec":
                print("Output: \t ", 1/math.sin(angle))
            elif func == "sec":
                print("Output: \t ", 1/math.cos(angle))
            elif func == "sinh":
                print("Output: \t ", math.sinh(angle))
                break
            elif func == "sech":
                print("Output: \t ", 1/math.cosh(angle))
            elif func == "cosech":
                print("Output: \t ", 1/math.sin(angle))
            elif func == "coth":
                print("Output: \t ", 1/math.tan(angle))
            elif func == "cosh":
                print("Output: \t ", math.cosh(angle))
                break
            elif func == "tanh":
                print("Output: \t ", math.tanh(angle))
                break
            else:
                print("Wrong Input! Try again.")
    if choice == 4:
        print('''
        ==============================================================================================POLYNOMIAL DERIVATIVE CALCULATOR==================================================================================
        ''')
        l = []
        degree = int(input("Enter degree(highest power of x) of equation: \t"))
        for i in range(degree):
            print("co-effecient of x power", degree - i, end="\t")
            l.append(int(input()))
        for i in range(degree):
            l[i] = l[i] * (degree - i)
        print("Output: \t ",end="")
        for i in range(degree):
            if i == (degree - 1):
                print(l[i],"x^",degree-(i+1), sep = "",end=" ")
            else:
                print(l[i],"x^",degree-(i+1), sep = "",end=" + ")
    while True:
        again = input("Do you want to use my calculator again? Y for yes, N for no: \t").upper()
        if again == 'N':
            flag = False
            break
        elif again =='Y':
            flag = True
            break
        else:
            print("Error. Enter either Y or N.")