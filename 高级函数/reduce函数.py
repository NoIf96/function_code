# -*- coding:utf-8 -*-
from functools import reduce

'''
    reduce(function, sequence)
        function 一个函数对象
        sequence 一个序列
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算
'''

def add(x, y):
    return x + y


def fn(x, y):
    return 10 * x + y


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    s = reduce(add, a)  #
    print(s)    #15
    x = reduce(fn, a)
    print(x)    #12345
