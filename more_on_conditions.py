# if 后面可以有更多的表达式，而不仅仅时时比较

# 比较可以链接起来
a, b, c = 3, 2, 2
if a > b == c :
    print('a大于b，并且b等于c')

# 可以用多个or来表示或，空串也会被表示成False
string1, string2, string3 = '', '', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

if '' :
    print('哈哈哈哈')