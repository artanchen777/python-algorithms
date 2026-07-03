funcs = []

for i in range(3):
    funcs.append(lambda: i)
    
print([f() for f in funcs])