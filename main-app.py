from calculator import Calculator
import decimal
import math

global mem
mem = 0

<<<<<<< HEAD
class Calculator(object):
    def add(self, num1, num2):
        answer = num1 + num2
        print("sum:", answer)
        return answer

    def sub(self, num1, num2):
        answer = num1 - num2
        print('Difference = ', answer)
        return answer
    def mul(self, num1, num2):
        answer = num1 * num2
        print('Multiplication = ', answer)
        return answer
    def div(self, num1, num2):
        if num2 != 0:
            print('Division = ', (num1 / num2))
            return (num1/num2)
        else:
            print("Err")
    def powerof(self, num, raiseby):
        answer = math.pow(num, raiseby)
        print('%f ^ %f = %f' % (num, raiseby, answer))
        return answer
    def square(self, num):
        answer = math.pow(num, 2)
        print(answer)
        return answer
    def squareroot(self, num):
        answer = math.sqrt(num)
        print("Square root (%f) = %f" % (num, answer))
        return answer
    def inverse(self, num):
        answer = 1/(num)
        print('Inverse (%f) = %f' % (num, answer))
        return answer
    def switchsign(self, num):
        print(1-(num<=0))
        return answer
    def sinrad(self, num):
        answer = math.sin(num)
        print('Sine (%f) = %f' %(num, answer))
        return answer
    def cosrad(self, num):
        answer = math.cos(num)
        print('Cosine (%f) = %f' %(num, answer))
        return answer
    def tanrad(self, num):
        answer = math.tan(num)
        print('Tangent (%f) = %f' %(num, answer))
        return answer
    def cosecrad(self, num):
        answer = 1/(math.sin(num))
        print('Inverse Sine(%f) = %f' % (num, answer))
        return answer
    def secrad(self, num):
        answer = 1/(math.cos(num))
        print('Inverse Cosine(%f) = %f' % (num, answer))
        return answer
    def cotrad(self, num):
        answer = 1/(math.tan(num))
        print('Inverse Tangent(%f) = %f' % (num, answer))
        return answer
    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        print('Sin(%f) in Degrees = %f' % (num, answer))
        return answer
    def cosdeg(self, num):
        answer = math.cos(math.radians(num))
        print('Cos(%f) in Degrees = %f' % (num, answer))
        return answer
    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        print('Tan(%f) in Degrees = %f' % (num, answer))
        return answer
    def cosecdeg(self, num):
        answer = 1/(math.sin(math.radians(num)))
        print('Inverse Sine(%f) in Degrees = %f' % (num, answer))
        return answer
    def secdeg(self, num):
        answer = 1/(math.cos(math.radians(num)))
        print('Inverse Cosine(%f) in degrees = %f' % (num, answer))
        return answer
    def cotdeg(self, num):
        answer = 1/(math.tan(math.radians(num)))
        print('Inverse Tangent(%f) in degrees = %f' % (num, answer))
        return answer
    def factorial(self, num):
        answer = math.factorial(num)
        print('Factorial (%f) = %f' % (num, answer))
        return answer
    def ln(self, num):
        answer = math.log(num)
        print('Log (%f) = %f' % (num, answer))
        return answer
    def logten(self, num):
        answer = math.log10(num)
        print('Log10(%f) = %f' % (num, answer))
        return answer
    def logbasex(self, num, x):
        answer = math.log(num, x)
        print('Log base (%f)(%f) = %f' % (x, num, answer))
        return answer
    def pie(self):
        print('pi = ', math.pi)
        return answer
    def e_constant(self):
        print('e = ', math.e)
        return answer

cal = Calculator()


def contin(y):
    cal = Calculator()
    cont = int(input("If you would like to stop type 1\nIf you would like to contine type 2\n"))
    if cont == 1:
       switchdisplaymode(y)
    elif cont == 2:
        fun = int(input("1 : Addition \t\t 2 : Subtraction\n3 : Multiplication \t 4 : Division\n5 : Square root \t 6 : Squared\n7:  Invert Sign\n"))
        contined(fun,y)
    else:
        print("Sorry try again")
        contin(y)

def contined(picked,y):
    if picked == 1:
        x = input("What number would you like to add?\n")
        num2 = test_answer(x,"add", "next")
        z = cal.add(int(y),int(num2))
        contin(z)
    elif picked == 2:
        x = input("What number would you like to add?\n")
        num2 = test_answer(x, "subtract", "next")
        z = cal.sub(int(y),int(num2))
        contin(z)
    elif picked == 3:
        x = input("What number would you like to multiply by?\n")
        num2 = test_answer(x, "multiply by", "next")
        z = cal.mul(int(y), int(num2))
        contin(z)
    elif picked == 4:
        x = input("What number would you like to add?\n")
        num2 = test_answer(x, "divide by", "next")
        z = cal.div(int(y), int(num2))
        contin(z)
    elif picked == 5:
        z = cal.squareroot(int(y))
        contin(z)
    elif picked == 6:
        z = cal.square(int(y))
        contin(z)
    elif picked == 7:
        z = y*-1
        print (z)
        contin(z)

def switchdisplaymode(x):
    displaypick = int(input("What display would you like to use?\n 1. Binary\n 2. Octal\n 3. Decimal\n 4. Hexadecimal\n 5. Continue to Memory \n"))
    convertdisplay(displaypick,x)

def convertdisplay(l,ber):
    ber = int(ber)
    if l == 1:
        b = bin(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 2:
        b = oct(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 3:
        b = decimal.Decimal(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 4:
        b = hex(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 5:
        memory_ask(ber)

def memory_clear():
    global mem
    mem = 0
    print_options()
def memory_recall():
    global mem
    print(str(mem) + " is in memory")
    int(mem)
    print_options()

def print_options():
    print("List of choice:")
    print('-' * 20)
    print("1 : Addition \t\t  12 : Sine in degrees")
    print("2 : Subtraction \t  13 : Cosine in degrees")
    print("3 : Multiplication \t  14 : Tan in degrees")
    print("4 : Division \t\t  15 : Cosecant in degrees")
    print("5 : Sine in radians \t  16: Secant in degrees")
    print("6 : Cosine in radians \t  17 : cot in degrees")
    print("7 : Tan in radians \t  18 : Natural log")
    print("8 : Cosecant in radians   19 : Base 10 log")
    print("9 : Secant in radians \t  20 : Log base'x'")
    print("10 : Cot in radians \t  21 : Square root")
    print("11 : pi \t\t  22 : Power of")
    print("MRC : To recall memory    M+ : To use number stored in memory")
    print("MC : to Clear Memory      ^C : to Power off   ")
    print('-' * 20)


def memory_ask(x):
    response = input("Would you like to store this number in memory? Y/N\n")
    if response == "Y":
        global mem
        mem = x
        print_options()
    elif response== "N":
        cal = Calculator()
        print_options()
    else:
        memory_ask(x)




def memory_use(memory):
    global mem
    print(str(mem) + " in memory")
    mem = int(mem)
    choice = ""
    print_options()
    choice = ""
    try:
        choice = input("Enter the number of choice: ")
        if choice == "MC" or choice == "M+" or choice == "MRC":
            str(choice)
        else:
            choice = int(choice)
    except ValueError:
        print("Enter a valid number: ")
    if choice == 1:
        y = input("Enter the second number to add : ")
        n2 = test_answer(y, "to add", "second")
        x = cal.add(mem, n2)
        contin(x)
    elif choice == 2:
        n1 = mem
        y = input("Enter the second number to subtract : ")
        n2 = test_answer(y, "to subtract", "second")
        x = cal.sub(mem, n2)
        contin(x)
    elif choice == 3:
        n1 = mem
        y = input("Enter the second number to multiply : ")
        n2 = test_answer(y,"to multiply","second")
        x = cal.mul(mem, n2)
        contin(x)
    elif choice == 4:
        n1 = memory
        y = input("Enter the second number for division : ")
        n2 = test_answer(y,"for division", "second")
        x = cal.div(mem, n2)
        contin(x)
    elif choice == 5:
        n = mem
        x = cal.sinrad(n)
        contin(x)
    elif choice == 6:
        n = memory
        x = cal.cosrad(n)
        contin(x)
    elif choice == 7:
        n = memory
        x = cal.tanrad(n)
        contin(x)
    elif choice == 8:
        n = memory
        x = cal.cosecrad(n)
        contin(x)
    elif choice == 9:
        n = memory
        x = cal.secrad(n)
        contin(x)
    elif choice == 10:
        n = memory
        x = cal.cotrad(n)
        contin(x)
    elif choice == 11:
        x = cal.pie()
        contin(x)
    elif choice == 12:
        n = memory
        x = cal.sindeg(n)
        contin(x)
    elif choice == 13:
        n = memory
        x = cal.cosdeg(n)
        contin(x)
    elif choice == 14:
        n = memory
        x = cal.tandeg(n)
        contin(x)
    elif choice == 15:
        n = memory
        x = cal.cosecdeg(n)
        contin(x)
    elif choice == 16:
        n = memory
        x = cal.secdeg(n)
        contin(x)
    elif choice == 17:
        n = memory
        x = cal.cotdeg(n)
        contin(x)
    elif choice == 18:
        n = memory
        x = cal.ln(n)
        contin(x)
    elif choice == 19:
        n = memory
        x = cal.logten(n)
        contin(x)
    elif choice == 20:
        n1 = memory
        n2 = input("Enter a number to find its log to this given log value : ")
        x = cal.logbasex(n1, n2) # steps are made like functions
        contin(x)
    elif choice == 21:
        n = memory
        x = cal.squareroot(n)
        contin(x)
    elif choice == 22:
        n1 = memory
        y = input("Enter a number to serve as exponent : ")
        n2 = test_answer(y, "Enter a number to serve as exponent", "")
        x = cal.powerof(n1, n2)
        int(x)
        contin(x)
    elif choice == "MC":
        memory_clear()
    elif choice == "M+":
        mem
        int(mem)
        memory_use(mem)
    elif choice == "MRC":
        memory_recall()
    else:
        print("ERROR : Please enter a valid number")

def test_answer(x, funct, place):
    while type(x) == str:
=======
def getFirstNumber():
    a = input("first number? ")
    while type(a) == str:
>>>>>>> 819cd30628996e546d87d7019a3bd708935bd87c
        try:
            a  = float(a)
        except ValueError:
            print("Error: Please Enter Valid number\n")
            a = getFirstNumber()
    return a

def getSecondNumber():
    b = input("second number? ")
    while type(b) == str:
        try:
            b  = float(b)
        except ValueError:
            print("Error: Please Enter Valid number\n")
            b = getSecondNumber()
    return b

def getTwoNumbers():
    a = getFirstNumber()
    b = getSecondNumber()
    return a, b


def displayResult(x: float):
    print(x, "\n")
    return x

def printOptions():
    print("List of choice:")
    print('-' * 60)
    print("Add\t  \t\t   Sine in degrees")
    print("Subtract   \t \t   Cosine in degrees")
    print("Multipy \t \t   Tan in degrees")
    print("Division \t\t   Cosecant in degrees")
    print("Sine in radians \t   Secant in degrees")
    print("Cosine in radians \t   Cotangent in degrees")
    print("Tangent in radians \t   Natural log")
    print("Cosecant in radians  \t   Base 10 log")
    print("Secant in radians \t   Log base'x'")
    print("Cotangent in radians \t   Square root")
    print("Squared \t\t   Exponent")
    print("Inverse \t\t   Switch sign")
    print("Factorial \t\t")
    print("B : For Binary View \t   O : For Octal View")
    print("D : For Decimal View\t   H : For Hexidecimal View")
    print("R: Degree to Radians\t   D: Radians to Degrees")
    print("M+ : Add to Memory   MRC : Add Memory to Display")
    print("MRC: Set Memory to 0")
    

def performFirstCalcLoop(calc):
    while True:
        printOptions()
        print("q to quit")
        print('-' * 60)
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'Add':
            a, b = getTwoNumbers()
            x = displayResult(calc.add(a, b))

        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.sub(a, b))

        elif choice == 'Multiply':
            a, b = getTwoNumbers()
            x = displayResult(calc.mul(a, b))

        elif choice == 'Division':
            a, b = getTwoNumbers()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print("Cannot Divide by zero")
                performFirstCalcLoop(calc)

        elif choice == 'Exponent':
            print("First number is base, Second is Exponent")
            a, b = getTwoNumbers()
            x = displayResult(calc.powerof(a, b))

        elif choice == 'Squared':
            a = getFirstNumber()
            x  = displayResult(calc.square(a))

        elif choice == 'Square root':
            a  = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == 'Inverse':
            a  = getFirstNumber()
            x = displayResult(calc.inverse(a))

        elif choice == 'Switch sign':
            a  = getFirstNumber()
            x = displayResult(calc.switchsign(a))

        elif choice == 'Sine in radians':
            a  = getFirstNumber()
            x = displayResult(calc.sinrad(a))

        elif choice == 'Cosine in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cosrad(a))


        elif choice == 'Tangent in radians':
            a  = getFirstNumber()
            x = displayResult(calc.tanrad(a))

        elif choice == 'Cosecant in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cosecrad(a))

        elif choice == 'Secant in radians':
            a  = getFirstNumber()
            x = displayResult(calc.secrad(a))

        elif choice == 'Cotangent in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cotrad(a))

        elif choice == 'Sine in degrees':
            a  = getFirstNumber()
            x =displayResult(calc.sindeg(a))

        elif choice == 'Cosine in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cosdeg(a))

        elif choice == 'Tangent in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.tandeg(a))

        elif choice == 'Cosecant in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cosecdeg(a))

        elif choice == 'Secant in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.secdeg(a))

        elif choice == 'Cotangent in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            a  = getFirstNumber()
            x = displayResult(calc.factorial(a))

        elif choice == 'Natural log':
            a  = getFirstNumber()
            x = displayResult(calc.ln(a))

        elif choice == 'Base 10 log':
            a  = getFirstNumber()
            x = displayResult(calc.logten(a))

        elif choice == 'Log base x':
            print("Second number is log base")
            a, b = getTwoNumbers()
            x = displayResult(calc.logbasex(a,b))
        elif choice == 'B':
            a = getFirstNumber()
            x = displayResult(bin(int(a)))
            x = a

        elif choice == 'O':
            a = getFirstNumber()
            x = displayResult(oct(int(a)))
            x = a

        elif choice == 'D':
            a = getFirstNumber()
            x = displayResult(decimal.Decimal(a))
            x = a

        elif choice == 'H':
            a = getFirstNumber()
            x = displayResult(hex(int(a)))
            x = a

        elif choice == 'R':
            a = getFirstNumber()
            x = displayResult(math.degrees(a))

        elif choice == 'D':
            a = getFirstNumber()
            x = displayResult(math.radians(a))

        elif choice == 'M+':
            global mem
            mem = x

        elif choice == "MC":
            mem = 0

        elif choice == "MRC":
            x = mem

        else:
            print("That is not a valid input.")
            performFirstCalcLoop(calc)

        performCalcLoop(calc, x)

def performCalcLoop(calc,a):
    x = a
    while True:
        printOptions()

        print("c to clear")
        print('-' * 60)
        print(str(a) + " is your first number\n")
        choice = input("Operation? ")
        if choice == 'c':
            break  # user types q to quit calulator.
        elif choice == 'Add':
            b = getSecondNumber()
            x = displayResult(calc.add(a, b))

        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.sub(a, b))

        elif choice == 'Multiply':
            b = getSecondNumber()
            x = displayResult(calc.mul(a, b))

        elif choice == 'Division':
            b = getSecondNumber()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print("Cannot Divide by Zero")
                performCalcLoop(calc,a)

        elif choice == 'Exponent':
            print("First number is base, Second is Exponent")
            b = getSecondNumber()
            x = displayResult(calc.powerof(a, b))

        elif choice == 'Squared':
            x  = displayResult(calc.square(a))

        elif choice == 'Square root':
            a  = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == 'Inverse':
            x = displayResult(calc.inverse(a))

        elif choice == 'Switch sign':
            x = displayResult(calc.switchsign(a))

        elif choice == 'Sine in radians':
            x = displayResult(calc.sinrad(a))

        elif choice == 'Cosine in radians':
            x = displayResult(calc.cosrad(a))


        elif choice == 'Tangent in radians':
            x = displayResult(calc.tanrad(a))

        elif choice == 'Cosecant in radians':
            x = displayResult(calc.cosecrad(a))

        elif choice == 'Secant in radians':
            x = displayResult(calc.secrad(a))

        elif choice == 'Cotangent in radians':
            x = displayResult(calc.cotrad(a))

        elif choice == 'Sine in degrees':
            x =displayResult(calc.sindeg(a))

        elif choice == 'Cosine in degrees':
            x = displayResult(calc.cosdeg(a))

        elif choice == 'Tangent in degrees':
            x = displayResult(calc.tandeg(a))

        elif choice == 'Cosecant in degrees':
            x = displayResult(calc.cosecdeg(a))

        elif choice == 'Secant in degrees':
            x = displayResult(calc.secdeg(a))

        elif choice == 'Cotangent in degrees':
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            x = displayResult(calc.factorial(a))

        elif choice == 'Natural log':
            x = displayResult(calc.ln(a))

        elif choice == 'Base 10 log':
            x = displayResult(calc.logten(a))

        elif choice == 'B':
            x = displayResult(bin(int(a)))
            x = a

        elif choice == 'O':
            x = displayResult(oct(int(a)))
            x = a

        elif choice == 'D':
            x = displayResult(decimal.Decimal(a))
            x = a

        elif choice == 'H':
            x = displayResult(hex(int(a)))
            x = a

        elif choice == 'R':
            x = displayResult(math.degrees(a))

        elif choice == 'D':
            x = displayResult(math.radians(a))

        elif choice == 'M+':
            global mem
            mem = x

        elif choice == "MC":
            mem = 0

        elif choice == "MRC":
            x = mem

        elif choice == 'Log base x':
            print("Second number is log base")
            b = getSecondNumber()
            x = displayResult(calc.logbasex(a,b))

        else:
            print("That is not a valid input.")

        performCalcLoop(calc, x)

# main start
def main():
    calc = Calculator()
    performFirstCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()