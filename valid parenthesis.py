# invalid parenthesis
"""s=input()
b=True
for i in range(0,len(s)-1,2):
    if(s[i] in [')','}',']'] and  b):
        print("invalid parenthesis")
        break
    elif((s[i]=='(' and s[i+1]!=')') or (s[i]=='{' and s[i+1]!='}') or (s[i]=='[' and s[i+1]!=']')):
        print("invalid parenthesis")
        b=False
        break
else:
    print("valid parenthesis")"""

s = input()
s1 = s[: len(s) // 2]
s2 = s[len(s) // 2 :][::-1]
b = True
for i in range(len(s1)):
    if s1[i] in [")", "]", "}"] and b:
        print("invalid parenthesis")
        break
    elif (
        s1[i] == "("
        and s2[i] != ")"
        or s1[i] == "["
        and s2[i] != "]"
        or s1[i] == "{"
        and s2[i] != "}"
    ):
        print("invalid parenthesis")
        break
else:
    print("valid parenthesis")
