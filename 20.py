"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

"""
if character is (, [ or { then push on stack 

[
(

else compare with top of the stack, if it's the closing then pop the top of the stack
"""


def isValid(s: str) -> bool:
    mapping = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in mapping.keys():
            stack.append(c)
        else:
            if not stack:
                return False 
            if mapping[stack.pop()] != c:
                return False 
    return not stack

