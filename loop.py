# for 循环中的break

for n in range(2, 10) : 
    for x in range(2, n) :
        if n % x == 0 : 
            print(n, 'equal', x, '*', n//x)
            break
    else : # for 循环的else，当正常循环结束时会调用这个方法，当break的时候不会调用
        print(n, 'is a prime number')

# for else
isBreak = True
for i in range(20) :
    if isBreak and i > 10 :
        break
    print(i)
else :
    print('正常循环结束，没有break')

# 循环也支持continue
for n in range(2, 10) :
    if n % 2 == 0 : 
        print("Found an even number", n)
        continue
    print("Found a number", n)