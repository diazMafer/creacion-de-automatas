from graphviz import Digraph
import re

class Transition:
    def __init__(self, start, transition, end):
        self.start = start
        self.transition = transition
        self.end = end

class StackElement:
    def __init__(self, q, expression, alphabet, q0, f, transitions):
        self.q = q
        self.expression = expression
        self.alphabet = alphabet
        self.q0 = q0
        self.f=f
        self.transitions = transitions

def thompson_alg(postfix):
    stack = []
    counter = 0
    char_counter = 0

    for c in postfix:
        if (c != '(') and (c != ')')  and (c != '*') and (c != '|') and (c != '.'):
            state1 = 'q' + str(counter)
            state2 = 'q' + str(counter+1)
            states = [state1, state2]
            counter+=2
            transition = Transition(start=state1, transition=c, end=state2)
            transitions = [transition]
            element = StackElement(q=states, expression=c, alphabet=[c], q0=state1, f=state2, transitions=transitions)
            stack.append(element)

        else:
            if (c == '|'):
                element2=stack.pop()
                element1=stack.pop()
                initial_state = 'q' + str(counter)
                final_state = 'q' + str(counter+1)
                counter+=2
                transition1 = Transition(start=initial_state, transition='e', end=element1.q0)
                transition2 = Transition(start=initial_state, transition='e', end=element2.q0)
                transition3 = Transition(start=element1.f, transition='e', end=final_state)
                transition4 = Transition(start=element2.f, transition='e', end=final_state)

                old_transitions = element1.transitions + element2.transitions
                new_transitions = [transition1, transition2, transition3, transition4]
                current_transitions = old_transitions + new_transitions

                old_states = element1.q + element2.q
                new_states = [initial_state, final_state]
                current_states = old_states + new_states

                current_expression = '(' + element1.expression + '|' + element2.expression + ')'
                current_alphabet = element1.alphabet + element2.alphabet

                element = StackElement(q=current_states, expression=current_expression, alphabet=current_alphabet, q0=initial_state, f=final_state, transitions=current_transitions)
                stack.append(element)

            if (c == '.'):
                element2=stack.pop()
                element1=stack.pop()

                new_transitions = []
                element2_transitions = []
                
                for transition in element2.transitions:
                    if transition.start == element2.q0:
                        transition1 = Transition(start=element1.f, transition=transition.transition, end=transition.end)
                        new_transitions.append(transition1)
                    else:
                        element2_transitions.append(transition)    


                old_transitions = element1.transitions + element2_transitions
                current_transitions = old_transitions + new_transitions

                old_states = element1.q + element2.q
                current_states = []

                for state in old_states:
                    if state != element2.q0:
                        current_states.append(state)

                current_expression = '(' + element1.expression + '.' + element2.expression + ')'
                current_alphabet = element1.alphabet + element2.alphabet        

                element = StackElement(q=current_states, expression=current_expression, alphabet=current_alphabet, q0=element1.q0, f=element2.f, transitions=current_transitions)
                stack.append(element)

            if (c == '*'):
                element = stack.pop()
                initial_state = 'q' + str(counter)
                final_state = 'q' + str(counter+1)
                counter+=2
                transition1 = Transition(start=initial_state, transition='e', end=element.q0)
                transition2 = Transition(start=element.f, transition='e', end=final_state)
                transition3 = Transition(start=initial_state, transition='e', end=final_state)
                transition4 = Transition(start=element.f, transition='e', end=element.q0)

                old_transitions = element.transitions 
                new_transitions = [transition1, transition2, transition3, transition4]
                current_transitions = old_transitions + new_transitions

                old_states = element.q 
                new_states = [initial_state, final_state]
                current_states = old_states + new_states

                current_expression = '(' + element.expression + ')*'
                current_alphabet = element.alphabet

                element = StackElement(q=current_states, expression=current_expression, alphabet=current_alphabet, q0=initial_state, f=final_state, transitions=current_transitions)
                stack.append(element)

    last = stack.pop()
    for state in last.q: 
        print(state + ', ') 

    for char in last.alphabet:
        print(char + ', ')    
    
    print(last.q0) 

    print(last.f) 

    for transition in last.transitions:
        print('('+transition.start+', '+transition.transition+', '+transition.end+'), ') 
    return (last)


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

def generateTXT(afn):
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






