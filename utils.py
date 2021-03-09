
from thompson import *
import re
from subsets import *


def precedence(op):
    if op == '|':
        return 1
    if op == '.':
        return 2
    if op == '*':
        return 3
    return 0

def expand(expression):
    r = ""
    counter = 0
    for character in expression:
        if character == "|":
            counter = 0
        elif character == "(":
            if counter == 1 :
                r = r + "." 
                counter = 0
                print("entre1")
        elif character == ")" or character == "*" or character == ".":
            pass
        else:
            counter += 1
        if counter == 2:
            r = r + "." + character
            counter = 1
        else:
            r = r + character
    
    return r


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

def graphicAFN(afn):
    f = Digraph('finite_state_machine', filename='afn.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    f.node(afn.q0)
    f.node(afn.f)

    f.attr('node', shape='circle')
    for transition in afn.transitions:
        f.edge(str(transition.start), str(transition.end), label=str(transition.transition))
    f.view()

def graphicAFD(afn):
    f = Digraph('finite_state_machine', filename='afd.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    f.node(afn.q0)
    f.node(afn.f)

    f.attr('node', shape='circle')
    for transition in afn.transitions:
        f.edge(str(transition.start), str(transition.end), label=str(transition.transition))
    f.view()

def gen_afn_txt(afn):
    f = open('afn.txt', 'w+')
    f.write("Estados = {")
    for state in afn.q: 
        f.write(state + ',') 
    f.write("}")
    f.write('\n')

    f.write("Simbolos = {")
    for char in afn.alphabet:
        f.write(char + ',')
    f.write("}")    
    f.write('\n')
    
    f.write("Inicio: " + afn.q0) 
    f.write('\n')

    f.write("Aceptacion: " + afn.f) 
    f.write('\n') 

    f.write("Transiciones: ")
    f.write('\n')
    for transition in afn.transitions:
        f.write('('+transition.start+', '+transition.transition+', '+transition.end+'), ') 

def gen_afd_txt(afn):
    f = open('afd.txt', 'w+')
    f.write("Estados = {")
    for state in afn.q: 
        f.write(str(state) + ',') 
    f.write("}")
    f.write('\n')

    f.write("Simbolos = {")
    for char in afn.alphabet:
        f.write(str(char) + ',')
    f.write("}")    
    f.write('\n')
    
    f.write("Inicio: " + str(afn.q0)) 
    f.write('\n')

    f.write("Aceptacion: " + str(afn.f)) 
    f.write('\n') 

    f.write("Transiciones: ")
    f.write('\n')
    for transition in afn.transitions:
        f.write('('+str(transition.start)+', '+str(transition.transition)+', '+str(transition.end)+'), ') 


expression = input('Enter infix expression')
print('infix expression: ',expression)
expanded = expand(expression)
print('expanded version: ', expanded)
converted = parseExp(expanded)
print('converted expression: ', converted)
postfix = evaluate(converted)
print('postfix expression: ', postfix)
afn = thompson_alg(postfix)
graphicAFN(afn)
gen_afn_txt(afn)
dfa = dfa_nfa(afn)
graphicAFD(dfa)
gen_afd_txt(dfa)






            
    



