s = "sample {  india is grest [ yes it is (by two distance)] sample code{ this is inside}}"
#s = "])}"
stack = []
for i in range(len(s)):
    current = s[i]
    if(current=='{' or current == '[' or current == '('):
        stack.append(current)
    
    if(current=='}' or current == ']' or current == ')'):
        if(len(stack) == 0):
            print "parenthesis not in order"
            break
        last = stack[len(stack)-1]
        if((last == '{' and current == '}') or (last == '[' and current == ']') or (last == '(' and current == ')')):
            stack.pop()
        else:
            print "parenthesis not in order"
            break
            
    if(i==len(s)-1 and len(stack) == 0):
        print "parenthesis are in order"