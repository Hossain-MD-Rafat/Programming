def isHappy(n):
    num = 0
    nh = set()
    nh.add(n)
    while 1:
        num += (n % 10) ** 2
        n = int(n / 10)
        if n != 0:
            continue
        if num == 1:
            return 1
        if num in nh:
            return 0
        nh.add(num)
        n = num
        num = 0


print(isHappy(19))

# notHappy = set()
# n = str(n)
# while n != '1':
#     notHappy.add(n)
#     nd = 0
#     for d in n:
#         nd += int(d) * int(d)
#     n = str(nd)
#     if n in notHappy:
#         return False
#
# return True







