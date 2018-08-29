# 其他类型比较

# 序列比较，会线从第一个元素开始比较，如果前面英确定了结果就不往下比较了
t1 = 1, 2, 3
t2 = 1, 2, 4
if t1 < t2 :
    print(t1, t2)

s1 = [1, 2, 3]
s2 = [1, 2, 4]
if s1 < s2 :
    print(s1, s2)

if 'ABC' < 'C' :
    print('ABC 小于 C')

def com_ver(v1='1.0.0', v2='1.0.0') :
    v1s = v1.split('.')
    v2s = v2.split('.')

    loop_count = 0
    for va, vb in zip(v1s, v2s) :

        if int(va) > int(vb) :
            return 1
        elif int(va) < int(vb) :
            return -1
        else :
            pass

        loop_count += 1
    else :
        if len(v1s) > loop_count :
            for n in v1s[loop_count:] :
                print('---', n, v1s, loop_count, v1s[loop_count:])
                if int(n) > 0 :
                    return 1
            else :
                return 0
        elif len(v2s) > loop_count : 
            for n in v2s[loop_count:] :
                if int(n) > 0 :
                    return -1
            else :
                return 0
        else :
            return 0

print(com_ver('1.0.0', '1.0.1'))
print(com_ver('10.0.0', '2.0.1'))
print(com_ver('1.2.10', '1.100.1'))
print(com_ver('1.0.10', '1.0.8'))
print(com_ver('1.0.10', '2.0.0'))
print(com_ver('100.200.003', '100.200.003'))
print(com_ver('1.0.0.1', '1.0.0'))