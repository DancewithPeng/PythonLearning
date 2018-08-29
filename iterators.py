# 迭代器
s = 'abc'
i = iter(s)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) 会抛出 StopIteration 异常，告诉迭代器迭代结束

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data): 
        self.data = data
        self.index = len(data)

    def __iter__(self): # 返回一个迭代器的对象
        return self

    def __next__(self): # 迭代器必须实现的next方法
        if self.index == 0:
            raise StopIteration # 迭代结束，抛出迭代结束的异常
        self.index = self.index - 1
        return self.data[self.index]

r = Reverse('123')        
d = iter(r)
print(d)
print(next(d))

for d in r :
    print(d)
    