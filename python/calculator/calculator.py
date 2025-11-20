def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0:
        return "Error: cannot divide by zero"
    return a/b

print("Simple Calculator")
while True:
    exp = input("Enter calculation (or q to quit): ")
    if exp.lower() == "q": break
    try:
        x, op, y = exp.split()
        x = float(x)
        y = float(y)
        if op == "+": print(add(x,y))
        elif op == "-": print(sub(x,y))
        elif op == "*": print(mul(x,y))
        elif op == "/": print(div(x,y))
        else: print("Invalid operator")
    except:
        print("Invalid format, use example: 5 + 2")
