# 标准库

# 操作系统
import os
cwd = os.getcwd() # 获取当前目录
print(cwd)
# os.chdir() 改变当前目录
# os.system('mkdir today') 进行系统命令

# dir() 和 help() 函数可以用作适用大型模块的辅助工具
#print(dir(os)) # 列出所有的os模块中的函数
#print(help(os)) # 导出模块中多数的文档

# 是处理文件和目录更好的工具
import shutil

# shutil.copyfile('data.db', 'archive.db') 拷贝文件
# shutil.move('/build/executables', 'installdir') 移动文件

# glob是用于查找统配文件符的工具
import glob
print(glob.glob('*.py')) # 列出所有py扩展名的文件

# 处理命令行参数
import sys
print(sys.argv) # 命令行参数是一个数组

# 退出程序
# sys.exit()

# 正则表达式模块
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) # 查找符合正则表达式的串

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')) # 子串

# 数学相关模块
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# 随机
import random
print(random.choice(['apple', 'pear', 'banana'])) # 随机选择一个元素
print(random.sample(range(100), 10)) # 随机取样，能保证不重复
print(random.random()) # 生成随机浮点数
print(random.randrange(6)) # 生成在范围内的随机整数

# 数据统计模块
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data)) # 平均数
print(statistics.median(data)) # 中间值
print(statistics.variance(data)) # 方差

# 网络请求
# from urllib.request import urlopen
# with urlopen('http://www.baidu.com') as response:
#     for line in response:
#         line = line.decode('utf-8')  # Decoding the binary data to text.        
#         print(line)

# 邮件
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()

# 时间处理
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")) # 小写是缩写，大写是全称

# 时间支持日历算法
birthday = date(1990, 6, 26)
age = now - birthday
print(age.days)

# 数据压缩
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

# 压缩后的数据
t = zlib.compress(s)
print(len(t))

src = zlib.decompress(t) # 解压
print(src)

print(zlib.crc32(s)) # CRC32校验

# 性能评估
from timeit import Timer
# 两只方式赋值方式需要的时间
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 测试
# def average(values) : 
#     """自动测试 

#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

# import doctest
# doctest.testmod() # 执行测试

# 单元测试，更完整的测试集
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests