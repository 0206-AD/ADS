def multiply(a,b):
    try:
        print("Multiplication is:",a*b)
    except:
        pass

def add(a,b):
    try:
        print("Addition is:",a+b)
    except:
        pass

def subtract(a,b):
    try:
        print("Subtraction is:",a-b)
    except:
        pass

def divide(a,b):
    try:
        print("Division is:",a/b)
    except:
        pass

def name():
    print("My name is Diaa")

def do():
    print("I can talk with you,I can do multiplication,addition,subtraction,\
division,lcm and hcf of any two numbers")

def up():
    print("Nothing much")

def how():
    print("I'm pretty good, How's your day? I hope everything is alright")

def hi():
    print("Hiii How are you?")

def ex():
    a=input("How was your experience with me? :").split()
    if 'great' in a or 'Great' in a or 'Good' in a or 'good' in a\
    or 'best' in a or 'Best' in a or 'better' in a or 'better' in a:
        print("Glad to hear :)")
    else:
        print("Sad to hear :(")

def start():
    print("Ya sure, What should i do first?")

def lcm(a,b):
    i=1
    while True:
        c=i*a
        if c%b==0:
            return c
        i+=1

def hcf(a,b):
        if a%b==0:
            return b
        elif b%a==0:
            return a
        elif a>b:
            return (hcf(a%b,b))
        else:
            return (hcf(a,b%a))

while True:
    try:
        a=input("Enter a text: ")
        if 'exit' in a or 'quit' in a:
            ex()
            x=input("Press enter to exit!!")
            break

        elif 'name' in a or 'Name' in a:
            name()
            continue

        elif 'do' in a or 'Do' in a:
            do()
            continue

        elif 'up' in a:
            up()
            continue

        elif 'bad' in a or 'Bad' in a or 'worse' in a or 'Worse' in a:
            print("Sad to hear :(")
            continue

        elif 'good' in a or 'fine' in a or 'Good' in a or 'Fine' in a\
        or 'best' in a or 'Best' in a or 'great' in a or 'Great' in a:
            print("That's amazing :)")
            continue

        elif 'hi' in a or 'Hi' in a or 'HI' in a or 'hello' in a\
        or 'Hello' in a:
            hi()
            continue

        elif 'how' in a or 'How' in a:
            how()
            continue

        elif 'start' in a or 'Start' in a:
            start()
            continue

        a=a.split()
        for i in range(0,len(a)):
            if '*' in a[i] or 'x' in a[i] or a[i]=='multiply' or a[i]=='multiplication' \
            or a[i]=='Multiply' or a[i]=='Multiplication' or a[i]=='*' or a[i]=='x':
                if ('*' in a[i] or 'x' in a[i])and(len(a[i])>1):
                    b=1
                    c=0
                    d=0
                    for j in range((len(a[i])-1),-1,-1):
                        if(a[i][j]=='*' or a[i][j]=='x'):
                            e=j
                            break
                        else:
                            d+=int(a[i][j])*b
                            b*=10
                    b=1
                    for j in range(e-1,-1,-1):
                        c+=int(a[i][j])*b
                        b*=10
                    multiply(c,d)
                elif a[i]+a[i+1]=='multiplyby' or a[i]+a[i+1]=='Multiplyby':
                    multiply(eval(a[i-1]),eval(a[i+2]))
                elif a[i]=='*' or a[i]=='x':
                    multiply(eval(a[i-1]),eval(a[i+1]))
                elif a[i]=='multiplication' or a[i]=='Multiplication':
                    multiply(eval(a[i+2]),eval(a[i+4]))
                else:
                    multiply(eval(a[i+3]),eval(a[i+1]))
                break

            elif a[i]=='+' or a[i]=='sum' or a[i]=='summation' or a[i]=='add' \
            or a[i]=='plus' or a[i]=='Plus' or a[i]=='addition' or a[i]=='Sum' \
            or a[i]=='Summation' or a[i]=='Add' or a[i]=='Addition' or '+' in a[i]:
                if '+' in a[i] and (len(a[i]) > 1):
                    b=1
                    c=0
                    d=0
                    for j in range((len(a[i])-1),-1,-1):
                        if(a[i][j]=='+'):
                            e=j
                            break
                        else:
                            d+=int(a[i][j])*b
                            b*=10
                    b=1
                    for j in range(e-1,-1,-1):
                        c+=int(a[i][j])*b
                        b*=10
                    add(c,d)
                elif a[i]=='plus' or a[i]=='Plus' or a[i]=='+':
                    add(eval(a[i+1]),eval(a[i-1]))
                elif a[i]=='sum' or a[i]=='summation' or a[i]=='addition' \
                or a[i]=='Sum' or a[i]=='Summation' or a[i]=='Addition':
                    add(eval(a[i+2]),eval(a[i+4]))
                else:
                    add(eval(a[i+1]),eval(a[i+3]))
                break

            elif a[i]=='-' or a[i]=='minus' or a[i]=='subtract' or a[i]=='Minus' \
            or a[i]=='Subtract' or a[i]=='subtraction' or a[i]=='Subtraction' or '-' in a[i]:
                if '-' in a[i] and (len(a[i]) > 1):
                    b=1
                    c=0
                    d=0
                    for j in range((len(a[i])-1),-1,-1):
                        if (a[i][j]=='-'):
                            e=j
                            break
                        else:
                            d+=int(a[i][j])*b
                            b*=10
                    b=1
                    for j in range(e-1,-1,-1):
                        c+=int(a[i][j])*b
                        b*=10
                    subtract(c,d)
                elif a[i]=='subtraction' or a[i]=='Subtraction':
                    subtract(eval(a[i+2]),eval(a[i+4]))
                elif a[i]=='-' or a[i]=='minus' or a[i]=='Minus':
                    subtract(eval(a[i-1]),eval(a[i+1]))
                else:
                    subtract(eval(a[i+1]),eval(a[i+3]))
                break

            elif a[i]=='/' or a[i]=='divided' or a[i]=='Divided' or a[i]=='divide' \
            or a[i]=='Divide' or a[i]=='division' or a[i]=='Division' or '/' in a[i]:
                if '/' in a[i] and (len(a[i]) > 1):
                    b=1
                    c=0
                    d=0
                    for j in range((len(a[i])-1),-1,-1):
                        if (a[i][j]=='/'):
                            e=j
                            break
                        else:
                            d+=int(a[i][j])*b
                            b*=10
                    b=1
                    for j in range(e-1,-1,-1):
                        c+=int(a[i][j])*b
                        b*=10
                    divide(c, d)
                elif a[i]=='divided' or a[i]=='Divided':
                    print(1)
                    divide(eval(a[i-1]),eval(a[i+2]))
                elif a[i]=='/':
                    print(2)
                    divide(eval(a[i-1]),eval(a[i+1]))
                elif a[i]=='division' or a[i]=='Division':
                    print(3)
                    divide(eval(a[i+2]),eval(a[i+4]))
                else:
                    print(4)
                    divide(eval(a[i+1]),eval(a[i+3]))
                break

            elif a[i]=='lcm' or a[i]=='LCM' or a[i]=='Lcm':
                print("LCM is:",lcm(int(a[i+2]),int(a[i+4])))
                break

            elif a[i]=='hcf' or a[i]=='HCF' or a[i]=='Hcf':
                print("HCF is:",hcf(int(a[i+2]),int(a[i+4])))
                break

        del a
    except:
        print("I didn't understand what you have written\nPlease repeat that again with proper syntax")
