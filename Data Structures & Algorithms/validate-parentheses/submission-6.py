class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {"[": "]", "(": ")", "{": "}"}

        for bracket in s:
            if bracket in brackets_dict:
                stack.append(bracket)
            else:
                if not stack or brackets_dict[stack[-1]] != bracket:
                    return False
                stack.pop()
        return not stack
             

        


        