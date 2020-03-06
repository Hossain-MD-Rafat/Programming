import re

num = int(input())
for i in range(num):
    str = input()
    enStr = ""
    for k in str:
        if re.match("[a-zA-Z]", k):
           enStr+= chr(ord(k)+3)
        else:
            enStr+=k
    enStr = enStr[::-1]
    ln = int(len(enStr)/2)
    first = enStr[0:ln]
    second = enStr[ln:]
    enSecond = ""
    for m in second:
        enSecond+=chr(ord(m)-1)
    encrypted=first+enSecond
    print(encrypted)