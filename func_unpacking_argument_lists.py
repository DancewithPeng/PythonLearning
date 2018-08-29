# 用 * 号在参数中解包list
def myMax(a, b) :
    if a > b :
        return a
    else :
        return b

print(myMax(1, 2))

arr = [3, 5]
print(myMax(*arr))


# 用**在参数中解包dict
def myMax2(x, y) :
    if x > y :
        return x
    else :
        return y

d = {'y': 20, 'x': 10}
print(myMax2(**d))