def balanced(expression):
    stack = []
    
    for char in expression:
        if char == "(":
            stack.insert(0, char)
        if char == ")":
            if "(" in stack:
                stack.pop()
            else:
                return False
    
    return False if stack else True

print(balanced(input()))