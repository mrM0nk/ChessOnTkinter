import time
n = int(input("Напечатайте_число_n "))
start = time.time()
a = [0]*(n+1)


def Показать_выражение():
    for i in range(1,n+1):
        if a[i]==0: print('(',end='')
        if a[i]==1: print(')',end='')
        if a[i]==2: print('{',end='')
        if a[i]==3: print('}',end='')
        if a[i]==4: print('[',end='')
        if a[i]==5: print(']',end='')
        if a[i]==6: print('<',end='')
        if a[i]==7: print('>',end='')
    print ()



def получилось_правильное_скобочное_выражение():
    Stack = []
    for i in range(1,n+1):
        skobka = a[i]
        if skobka in (0,2,4,6):
            Stack.append(skobka)
            continue

        if skobka in (1,3,5,7):
            if len(Stack) == 0:
                return False
            skobka_v_stacke = Stack.pop()
            if skobka_v_stacke != skobka - 1:
                return False
    if len(Stack) != 0:
        return False

    return True

р_д_у = n
while р_д_у >= 1:
    while (р_д_у >= 1) and (a[р_д_у] == 7):
        a[р_д_у] = 0
        р_д_у = р_д_у - 1

    if a[0] == 1 : break

    a[р_д_у] = a[р_д_у] + 1


    if a[-1] not in (0, 2, 4, 6) and a[1] not in (1, 3, 5, 7):
        if получилось_правильное_скобочное_выражение(): # v.1.0 21.37 s. 8 znakov,     10znakov 1412 s.
            Показать_выражение()
#    print(a)

    р_д_у = n

end = time.time()
print (str(round((end - start), 2)) + str(' sec.'))  # 35.65s 8 znakov
