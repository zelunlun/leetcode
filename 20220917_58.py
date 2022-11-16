s = 'Hello  World     you '
s1 = s.split()
print(len([test for test in [x for x in s1 if x != ''][-1]]))


diction = {'A':123, 'B':456}
print(diction['A'])