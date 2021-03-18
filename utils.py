
from thompson import *
import re
from subsets import move
from direct import directo
import tree 

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
    for character in expression:
        if character != "?" and character != "+":
            new.append(character)
            stack.append(character)
        elif character == "?":
            x = stack.pop()
            new.pop()
            new.append(str("("+x+"|e)"))
            stack = []
        elif character == "+":
            x = stack.pop()
            new.append(str("("+x+"*)"))
    
    print(new)
    
    return ''.join(new)
                    
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
    for node in afn.f:
        f.node(node)

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


def graphicDirect(afn):
    f = Digraph('finite_state_machine', filename='afd_direct.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    for node in afn.f:
        f.node(str(node))

    f.attr('node', shape='circle')
    for transition in afn.transitions:
        f.edge(str(transition.start), str(transition.end), label=str(transition.transition))
    f.view()

def simulation(expression, transitions, inicial_node, acceptance_states):
    i = 0
    inicial = inicial_node
    
    for character in expression:
        x = move(inicial, character, transitions)
        if len(x)==0:
            return "No"
        x = list(x)
        inicial = x[0]
    i = 0 
    for n in range(len(acceptance_states)):
        if inicial == acceptance_states[n]:
            i += 1
    if i !=0:
        return "Yes"
    else:
        return "No"

def simulationAFN(afn, expresion):
    if expresion == " ":
        expresion = "e"
    actual = [afn.q0]
    actual = cerradura(afn, actual)
    i = 0
    while True:
        temp = []
        for node in actual:
            for transition in afn.transitions:
                if transition.transition == expresion[i] and transition.end not in temp:
                    temp.append(transition.end)
        i += 1
        temp = cerradura(afn, temp)
        if not temp and expresion == "e":
            break
        actual = temp.copy()
        if i > len(expresion)-1:
            break
    for x in actual:
        if x == afn.f:
            return True
    return False
    
# encontrar transiciones epsilon en afn
def cerradura(afn, actual):
    for x in actual:
        for transition in afn.transitions:
            if transition.transition == "e" and transition.end not in actual:
                actual.append(transition.end)
    return actual









            
    



