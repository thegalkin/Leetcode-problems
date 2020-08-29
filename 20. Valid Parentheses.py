def isValid(s):
    s = "()[]{}"
    k = {"(": False, ")": False, "[": False, "]": False, "{": False, "}": False}
    uns = False
    for i in s:
        if i == "(":
            k["("] = True
            
        if i == ")":
            k[")"] = True

        if i == "[":
            k["["] = True

        if i == "]":
            k["]"] = True

        if i == "{":
            k["{"] = True

        if i == "}":
            k["}"] = True
        




print(isValid("()"))