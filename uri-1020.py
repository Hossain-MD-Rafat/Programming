while(True):
    str = input()
    [n, number] = str.split(" ")
    if(n=='0' and number=='0'):
        break
    else:
       number = '0' + number
       newstr = int(number.replace(n , ""))
       print(newstr)
