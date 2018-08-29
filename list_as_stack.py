# 列表作为栈
S = [1, 2, 3, 4, 5, 6]

# 入栈
S.append(66)
print(S)

# 出栈
e = S.pop()
print(e, S)

S.pop()
S.pop()
S.pop()

print(S)