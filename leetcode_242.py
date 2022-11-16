s = 'anagram'
t = 'nagaram'
# mylist = [x for x in t]
# for _ in s:
#     if _ in mylist:
#         continue
#     else:
#         print(False)
# print(True)

if len(s) != len(t):
    return False

diction = {}
for i in s :
    if i not in diction:
        diction[i] = 1
    else:
        diction[i] += 1
        
for n in t:
    if n not in diction:
        return False
    else:
        diction[n] -= 1
return True