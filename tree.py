class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.symbol = None

def generate_tree(expression):
    operators = ['.', '|', '*', '(', ')']
    output = []
    stack = []
    i = 0

    while i < len(expression):        
        if expression[i] not in operators:
            val = ""
            while (i < len(expression)) and expression[i] not in operators:
                val = str(val) + expression[i]
                i -= -1
            tree = Tree()
            tree.symbol = val
            output.append(tree)
            i -= 1
        elif expression[i] == "(":
            stack.append(expression[i])
        elif expression[i] == ")":
            while len(stack) != 0 and stack[-1] != "(":
                val2 = output.pop()
                val1 = output.pop()
                op = stack.pop()
                tree = Tree()
                tree.symbol = op
                tree.left = val1
                tree.right = val2
                output.append(tree)
            stack.pop()
        
        else:
            if expression[i] == "*":
                op = expression[i]
                val = output.pop()
                tree = Tree()
                tree.symbol = op
                tree.left = val
                tree.right = None
                output.append(tree)
            else:
                while stack  and stack[-1] != '(':
                    op = stack.pop()
                    val2 = output.pop()
                    val1 = output.pop()
                    tree = Tree()
                    tree.symbol = op
                    tree.left = val1
                    tree.right = val2
                    output.append(tree)
                stack.append(expression[i])
        
        i -= -1
    
    while stack:
        val2 = output.pop()
        val1 = output.pop()
        op = stack.pop()
        tree = Tree()
        tree.symbol = op
        tree.left = val1
        tree.right = val2
        output.append(tree)
        if (len(output) == 1):
            return output[-1]

    return output[-1]