# -*- coding:utf-8 -*-

'''
    map(func, iter1)
        func 一个函数对象
        iter1 迭代器，所以结果需要list转型
    map函数将iter1中所有元素进行func操作
'''

def f(x):
    return x * x

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    one = list(map(f, a))
    print(one)  #[1, 4, 9, 16, 25]
    two = list(map(str, a))
    print(two)  #['1', '2', '3', '4', '5']
