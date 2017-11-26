#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f(*args, **kwargs):
    print(args)
    print(kwargs)

def timeit(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('--start--')
        r = func(*args, **kwargs)
        print('--end--')
        return r
    return wrapper

## 引数から何かを計算して値を返すような関数 r = func(x,y) があったとする
## Nの依存性を調べたい．Nを増やして，計算量的にどう変わるか
## 値の情報も知りたい．値はそのまま返してもいいかも.(平均値を返す)
## N以外の引数はそのまま渡す
def runningtime(Ns, times=10):
    import timeit
    def _experiment(func):
        def wrapper(*args, **kwargs):
            print('# [run] args:', args, 'kwargs:', kwargs)
            print('\t'.join(['N', 'time', 'return']))
            for N in Ns:
                kwargs['N'] = N
                t = timeit.timeit(lambda: func(*args, **kwargs), number=times)/times
                r = func(*args, **kwargs)
                print('\t'.join(map(str, [N, t, r, '# {0} {1}'.format(args, kwargs)])))
            print('# [end]')
            return r
        return wrapper
    return _experiment

@runningtime([10**(i+1) for i in range(7)])
def test(x, y, N, sigma=10):
    # print('calculating N=', N, x, y, sigma)
    return N*x*y*sigma


if __name__ == '__main__':
    print('testcase')
    print('val', test(2, 3))
