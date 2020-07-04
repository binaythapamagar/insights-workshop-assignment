class Solution(object):
    
    def validateParenthesis(self,s):
        if s is None:
            return True
        
        stack = []
        
        for t in s:
            if t == ")":
                try:
                    current = stack.pop()
                    if current != '(':
                        return False   
                except:
                    return False
            elif t == "}":
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == "]":
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                stack.append(t)
                   
        if len(stack) == 0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    s = Solution()
    print('validating (){}[]')
    print(s.validateParenthesis("(){}[]"))
    print('validating {{))sssss')
    print(s.validateParenthesis("{{))"))