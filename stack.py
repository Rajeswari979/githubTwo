s = "12345*+-+"
num = []
sym = []
stack = []
for i in s:
    if i.isnumeric():
        num.append(i)
    else:
        sym.append(i)

num = num[::-1]
num = num+sym
for j in num:
    if j.isnumeric():
        stack.append(j)
    elif j == "*" or j== "+" or j=="-":
        if j == "*":
            first = stack.pop()
            second = stack.pop()
            op = int(first) * int(second)
            stack.append(op)
        elif j == "+":
            first = stack.pop()
            second = stack.pop()
            op = int(first) + int(second)
            stack.append(op)
        elif j == "-":
            first = stack.pop()
            second = stack.pop()
            op = int(first) - int(second)
            stack.append(op)
for k in stack:
    print(str(k))