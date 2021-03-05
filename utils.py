
def precedence(op):
    if op == '|':
        return 3
    if op == '.':
        return 1
    if op == '*':
        return 3
    return 0

#infix expression
def parseExp(expression):
    new = []
    stack = []
    counter = 0
    for character in expression:
        if character != "?" and character != "+":
            new.append(character)
        if character == "?" or character == "+":
            counter +=1
            if (character == "?" and new[-1] != ")") or (character == "+" and new[-1] != ")"):
                counter +=1
                x = True
                z = len(new)-1
                while x == True and z != -1:
                    if new[z] == ")" or new[z] == ".":
                        new.pop()
                        x = False
                    else:
                        stack.append(new[z])
                        new.pop()
                    z-=1
                if character == "?":
                    counter +=1
                    new.append(str("("+''.join(stack[::-1])+"|e)"))
                elif character == "+":
                    counter +=1
                    new.append(str("("+''.join(stack[::-1])+").("+''.join(stack[::-1])+"*)"))
                stack = []
            else: 
                v = len(new)-1
                z = True
                while z == True:
                    if new[v] == "(" :
                        stack.append("(")
                        new.pop()
                        z = False
                    else:
                        stack.append(new[v])
                        new.pop()
                    v-=1
                if character == "?":
                    counter +=1                    
                    new.append(str("("+''.join(stack[::-1])+"|e)"))
                elif character == "+":
                    counter +=1            
                    new.append(str("("+''.join(stack[::-1])+").("+''.join(stack[::-1])+"*"))
                stack = []
    
    print(new)
    i = 0
    final = list(new)
    if final[0] == ".":
        final.pop(0)
    
    return ''.join(final)
                    
def evaluate(expression):
    stack = []
    output = []
    operators = ['.', '|', '*', '(', ')']

    for character in expression:
        if character not in operators: 
            output.append(character)
        elif character == '(':
            stack.append(character)
        elif character == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence(character)<=precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(character)
    
    while stack:
        output.append(stack.pop())
    
    return output

expression = input('Enter infix expression')
print('infix expression: ',expression)
converted = parseExp(expression)
print('converted expression: ', converted)
postfix = evaluate(converted)
print('postfix expression: ', postfix)




            
    



