class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        # must be closed
        # order matters
        "()[]{}" -> true
        "([ ])" -> true
        
        
        
        "({[ ]}" -> true
        
        
        # ['(' ] -> stack 
        # ']' -> stack.pop() [
            } {
                stack will be empty -> we found all the opening for the closing ones
       
        #for (s):
            if opening:
                stack.add(s[i])
            else:
                # closing
                if stack.pop() != s[i]:
                    return False
        if stack is empty:
            return True
        return False
        """
        
        """
         "()[]{}"
         
        
        []
        """
        stack = []
    
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                # It's a closing one
                if len(stack) == 0:
                    return False
                else:
                    if s[i] == ']' and stack.pop() != '[':
                        return False
                    elif s[i] == '}' and stack.pop() != '{':
                        return False
                    elif s[i] == ')' and stack.pop() != '(':
                        return False   
        
        return len(stack) == 0
            
            
                
                    
        