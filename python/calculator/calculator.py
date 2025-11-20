# calculator.py
# Simple CLI calculator — supports + - * / and integer floats

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator — type 'q' to quit")
    while True:
        expr = input("Enter (e.g. 2 + 3): ").strip()
        if expr.lower() in ('q', 'quit', 'exit'): break
        try:
            parts = expr.split()
            if len(parts) != 3:
                print("Format: number operator number (e.g. 3 * 4)")
                continue
            a = float(parts[0]); op = parts[1]; b = float(parts[2])
            if op == '+': print("=", add(a,b))
            elif op == '-': print("=", sub(a,b))
            elif op == '*': print("=", mul(a,b))
            elif op == '/': print("=", div(a,b))
            else: print("Unknown operator. Use + - * /")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
