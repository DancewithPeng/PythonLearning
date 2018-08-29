import sys

try: 
    f = open('text.json')
    s = f.readline()
    i = int(s.strip())
except OSError as err :
    print("OS error: {0}".format(err))
except ValueError :
    print("Could not convert data to an integer.")
except : # 通配所有的异常
    print("Unexpected error:", sys.exc_info()[0])
    raise # 同时还可以把异常继续往外抛


# except还有一个else自子句，else在没有发生异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()