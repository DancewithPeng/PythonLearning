# 标准库第二部分

# reprlib用于显示大的数据集合，用于显示易于显示的样式
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# pprint用于自动显示漂亮的格式
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(t)
pprint.pprint(t, width=30) # 超过长度，会以比较合理的方式显示对应的对象

# textwrap用于合理得显示文本
import textwrap
doc = """
The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines.
"""
print(doc)
print(textwrap.fill(doc, width=40)) # 在指定宽度的屏幕中，合理显示段落

# locale用于本地化
# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# 字符串模版
from string import Template
t = Template('${village}folk send $$10 to $cause.') # 用$符号来表示占位符，如果需要显示$符号，则用'$$'表示
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t2 = Template('Return the $item to $owner.') 
print(t2.safe_substitute(item='1234')) # 用safe_substitute方法，如果字典中没有保护占位符的key，就回显示原本的占位符，而substitute则会抛异常

# 