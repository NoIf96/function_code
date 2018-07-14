# -*- coding:utf-8 -*-

'''
    返回函数
        将函数做为返回值返回
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

if __name__ == '__main__':
    f = lazy_sum(1, 2, 3, 4, 5)
    print(f) #<function lazy_sum.<locals>.sum at 0x000001D35A845AE8>
    print(f()) #15

