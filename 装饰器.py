# -*- coding:utf-8 -*-
import datetime

'''
    假设我们要增强某函数的功能，但又不希望修改函数的定义，
    这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(datetime.datetime.now())

if __name__ == '__main__':
    now()
