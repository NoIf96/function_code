# -*- coding:utf-8 -*-

'''
    filter(function, iterable)
        function 一个函数对象
        iterable 可迭代对象
    filter函数将iterable中所有元素进行function筛选
'''

def isOdd(n):
    return n % 2 == 1

def notEmpty(s):
    return s and s.strip()

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    odd = list(filter(isOdd, a))
    print(odd) #[1, 3, 5]
    s = list(filter(notEmpty, ['a', 'b', ' ', 'd', 'f', '  ']))
    print(s) #['a', 'b', 'd', 'f']
