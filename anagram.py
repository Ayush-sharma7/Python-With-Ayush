# anagram string
s1 = input("ENTER STRING 1: ").lower()
s2 = input("ENTER STRING 2: ").lower()
l, l2 = len(s1), len(s2)
s1, s2 = sorted(s1), sorted(s2)
for i in range(l):
    if s1[i] != s2[i]:
        print("not anagrams")
        break
else:
    print("anagrams")


# Alternative
"""from collections import Counter

s1 = input("ENTER STRING 1: ").lower()
s2 = input("ENTER STRING 2: ").lower()

if Counter(s1) == Counter(s2):
    print("anagrams")
else:
    print("not anagrams")"""