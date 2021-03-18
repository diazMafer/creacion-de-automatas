from thompson import *
import re
from subsets import subsets_alg
from direct import directo
from tree import generate_tree
from utils import *

ans = True
while ans:
    print("""
    1. Thompson Algorithm
    2. Subsets Algorithm
    3. Direct Algorithm
    4. All Algorithms
    5. Exit
    """)
    ans=input("What would you like to do? ") 

    if ans=="1": 
        expression = input('Enter infix expression')
        expression = expression.replace('ε','e')
        print('infix expression: ',expression)
        balanced = check(expression)
       
        if balanced != False:
            converted = parseExp(expression)
            print('converted expression: ', converted)
            expanded = expand(converted)
            print('expanded version: ', expanded)
            postfix = evaluate(expanded)
            print('postfix expression: ', postfix)
            afn = thompson_alg(postfix)
            graphicAFN(afn)
            gen_afn_txt(afn)
            exp_evaluate = input('Enter expression to evaluate ')
            print(simulationAFN (afn, exp_evaluate))
        else:
            print("Expression has an error")

    elif ans=="2":
        expression = input('Enter infix expression')
        expression = expression.replace('ε','e')

        print('infix expression: ',expression)
        balanced = check(expression)

        if balanced != False:
            converted = parseExp(expression)
            print('converted expression: ', converted)
            expanded = expand(converted)
            print('expanded version: ', expanded)
            postfix = evaluate(expanded)
            print('postfix expression: ', postfix)
            afn = thompson_alg(postfix)
            graphicAFN(afn)
            gen_afn_txt(afn)
            dfa = subsets_alg(afn)
            graphicAFD(dfa)
            gen_afd_txt(dfa)
            exp_evaluate = input('Enter expression to evaluate ')
            print(simulation(exp_evaluate, dfa.transitions, dfa.q0, dfa.f))
        else:
            print("Expression has an error")

    elif ans=="3":
        expression = input('Enter infix expression')
        expression = expression.replace('ε','e')
        print('infix expression: ',expression)
        balanced = check(expression)

        if balanced:
            converted = parseExp(expression)
            print('converted expression: ', converted)
            expanded = expand(converted)
            print('expanded version: ', expanded)
            tree = generate_tree(expanded)
            afd_direct = directo(tree, expanded)
            graphicDirect(afd_direct)
        else:
            print("Expression has an error")

    elif ans=="4":
        expression = input('Enter infix expression')
        expression = expression.replace('ε','e')
        print('infix expression: ',expression)
        balanced = check(expression)
        
        if balanced != False:
            converted = parseExp(expression)
            print('converted expression: ', converted)
            expanded = expand(converted)
            print('expanded version: ', expanded)
            postfix = evaluate(expanded)
            print('postfix expression: ', postfix)
            afn = thompson_alg(postfix)
            graphicAFN(afn)
            gen_afn_txt(afn)
            dfa = subsets_alg(afn)
            graphicAFD(dfa)
            gen_afd_txt(dfa)
            print("directo")
            tree = generate_tree(expanded)
            transitions = directo(tree, expanded)
            graphicDirect(transitions)
        else:
            print("Expression has an error")

    elif ans=="5":
        exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 