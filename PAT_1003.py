import re
n = input()
for i in range(int(n)):
    str = input()
    if re.match(r'A*PA+TA*', str):
        a = re.split(r'[P|T]',str)
        if len(a[0])*len(a[1]) == len(a[2]):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
