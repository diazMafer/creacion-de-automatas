from transition import *
from automata import *

def eclosure(step, transitions):
    if isinstance(step, int):
        nodes = []
        nodes.append(step)
    else: 
        nodes = list(step)
    if isinstance(nodes, list):
        for n in nodes:
            move = possible_movements(n, "e", transitions)
            for x in move:
                if int(x.end) not in nodes:
                    nodes.append(int(x.end))
    s = set()
    for item in nodes:
        s.add(item)
    return s

# return all moves
# nodes = nodos en el que se encuentra ahorita
# symbol = que letra vamos a mover
# transitions = nuestras transiciones
def move(nodes, symbol, transitions):
    nodes = list(nodes)
    moves = []
    if isinstance(nodes, list):
        for n in range(len(nodes)):
            posible_moves = possible_movements(nodes[n], symbol, transitions)
            for move in posible_moves:
                if int(move.end) not in moves:
                    moves.append(int(move.end))
        s = set()
        for item in moves:
            s.add(item)
        return s
    
    else:
        posible_moves = possible_movements(nodes, symbol, transitions)
        for move in posible_moves:
            if int(move.end) not in moves:
                moves.append(int(move.end))
                 
        s = set()
        for item in moves:
            s.add(item)
        return s

#shows possibles moves from a node and a symbol of the nfa
#node = node which we want to know moves
#symbols = symbol to use to find moves
#transitions = afn transitions
def possible_movements(node, symbols, transitions):
    moves = []
    for transition in transitions:
        if int(transition.start) == node and str(transition.transition) == str(symbols):
            moves.append(transition) 
    return moves


""" 
subset algorithm to convert nfa to dfa requires eclosure function and a function to know all
the possibles moves
"""

def subsets_alg(afn):
    alphabet = afn.alphabet
    for character in alphabet:
        if character == "e":
            alphabet.remove('e')
    print(alphabet)
    afn_pstates = [[int(afn.q0), int(afn.f)]]
                   
    i = 0
    dfa_state =[]
    table = []
    dfa_state.append(eclosure(int(afn.q0), afn.transitions))
    terminal_states =[]
    terminal_states.append(eclosure(int(afn.q0), afn.transitions))
    transitions_dfa = []
    
    while i < len(dfa_state):
        for n in alphabet:
            u = eclosure(move(dfa_state[i],n,afn.transitions),afn.transitions)
            transition = Transition(start=dfa_state[i], transition=n, end=u)
            transitions_dfa.append(transition)
            if (transition.start != set() and transition.end != set()):
                table.append(transition)
            for w in afn_pstates:
                if w[1] in u:
                    terminal_states.append(u)
            if u not in dfa_state and u is not None and u != set():
                dfa_state.append(u)         
        i+=1
    
    

    print("Proceso de cambio de NFA a DFA")
    
    for transition in table:
        print('('+str(transition.start)+', '+transition.transition+', '+str(transition.end)+'), ') 
    
    
    # assign a letter to each subset generated
    dfa_alphabet_nodes =["A","B","C","D","E","F","G","H","I","J"]
    for transition in table:
        start1 = dfa_state.index(transition.start)
        h = dfa_alphabet_nodes[start1]
        transition.set_start(start=h)
        start2 = dfa_state.index(transition.end)
        n = dfa_alphabet_nodes[start2]
        transition.set_end(end=n)
    
    
    for transition in table:
        print('('+str(transition.start)+', '+transition.transition+', '+str(transition.end)+'), ') 
    print(terminal_states)

    x = 0
    
    while x < len(terminal_states):
        indice1 = dfa_state.index(terminal_states[x])
        terminal_states[x]= dfa_alphabet_nodes[indice1]
        x+=1
   
    dfa = Automata(dfa_state, afn.expression, alphabet, terminal_states[0], terminal_states[1], table)
    return dfa

def simulation(expression, transitions, terminals):
    i = 0
    inicial = terminals[0][0]
    
    for character in expression:
        x = move(inicial, character, transitions)
        if len(x)==0:
            return "NO"
        x = list(x)
        inicial = x[0]
    i = 0 
    for n in range(len(terminals)):
        if inicial == terminals[n][1]:
            i += 1
    if i !=0:
        return "YES"
    else:
        return "NO"