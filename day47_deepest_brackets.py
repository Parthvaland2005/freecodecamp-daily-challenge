def get_deepest_brackets(s):
    
    stack = []
    max_depth = 0
    current = ""
    result = ""
    
    for ch in s:
        
        if ch in "([{":
            stack.append(ch)
            current = "" 
            
            if len(stack) > max_depth:
                max_depth = len(stack)
                result = ""   
        
        elif ch in ")]}":
            if len(stack) == max_depth:
                result = current   
            
            stack.pop()
            current = ""
        
        else:
            if len(stack) > 0:
                current += ch
    
    return result

print(get_deepest_brackets("(hello (world))"))  # world
print(get_deepest_brackets("[outer [inner] outer]"))  # inner
print(get_deepest_brackets("{a{b}c{d{e}f}g}"))  # e
print(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"))  # fox
print(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"))  # C