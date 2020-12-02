res=["Welcome to Smart Calculator","My name is Diaa","I can talk with you,I can do multiplication,addition,subtraction,\
division,lcm and hcf of any two numbers","Sorry, this is beyond my capability"]

def num(text):
    n=[]
    for t in text.split():
        try:
            n+=[eval(t)]
        except:
            pass
    return n

def lcm(a,b):
    i=1
    while True:
        c=i*a
        if c%b==0:
            return c
        i+=1

def hcf(a,b):
    h=a if a>b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def add(a,b):
    print("Addition is:",a+b)

def subtract(a,b):
    print("Subtraction is:",a-b)

def multiply(a,b):
    print("Multiplication is:",a*b)

def divide(a,b):
    print("Division is:",a/b)

def end():
    ex()
    print("Thanks",end=", ")
    input("Press Enter to quit ")
    exit(0)

def ex():
    a=input("How was your experience with me?: ")
    if 'great' in a or 'Great' in a or 'Good' in a or 'good' in a\
    or 'best' in a or 'Best' in a or 'better' in a or 'better' in a:
        print("Glad to hear :)")
    else:
        print("Sad to hear :(")

def name():
    print(res[1])

def do():
    print(res[2])

def up():
    print("Nothing much")

def how():
    print("I'm pretty good, How's your day? I hope everything is alright")

def hi():
    print("Hiii How are you?")

def start():
    print("Ya sure, What should i do first?")

def sorry():
    print(res[3])

op={"multiply":multiply,"multiplication":multiply,"*":multiply,"x":multiply,
    "sum":add,"summation":add,"add":add,"plus":add,"+":add,
    "minus":subtract,"subtract":subtract,"subtraction":subtract,"-":subtract,
    "divided":divide,"divide":divide,"division":divide,'/':divide,
    "lcm":lcm,"hcf":hcf}

cmd={"name":name,"name?":name,"do":do,"do?":do,'exit':end,'quit':end,"end":end,'close':end}

while True:
    print()
    text=input('Enter a text: ')
    for word in text.split():
        if word.lower() in op.keys():
            try:
                l=num(text)
                r=op[word.lower()](l[0],l[1])
            except:
                print("Something is wrong retry!")
            finally:
                break
        elif word.lower() in cmd.keys():
            cmd[word.lower()]()
            break
    else:
        sorry()
