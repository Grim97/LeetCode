'''
Method 1

def maxDepth(s: str) -> int:
    stack = list()
    depth = 0
    # stack = [stack.append(char) for char in s if char =='(']
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        depth = max(depth, len(stack))
    
    print(stack)
    return depth
'''

'''Method 2
'''
def maxDepth(s: str) -> int:
    max_depth = 0
    curr_depth = 0
    for char in s:
        if char == '(':
            curr_depth += 1
        elif char == ')':
            curr_depth -= 1
        max_depth = max(curr_depth, max_depth)
    
    # print(stack)
    return max_depth


st = "()(())((()()))"
print(maxDepth(st))