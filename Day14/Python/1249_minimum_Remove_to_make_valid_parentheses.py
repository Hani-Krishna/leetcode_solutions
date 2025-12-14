class Solution(object):
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # mark unmatched )

        for i in stack:  # unmatched (
            s[i] = ''

        return ''.join(s)
