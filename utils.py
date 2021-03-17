
from thompson import *
import re
from subsets import subsets_alg
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

    f.attr('node', shape='circle')
    for transition in afn:
        f.edge(str(transition.start), str(transition.end), label=str(transition.transition))
    f.view()









            
    



