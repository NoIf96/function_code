# -*- coding:utf-8 -*-

'''
    匿名函数 lamba
        参数：操作
'''

if __name__ == '__main__':
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    y = lambda x: x + 1
    print(y(6))
