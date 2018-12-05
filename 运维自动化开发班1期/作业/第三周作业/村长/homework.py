#No.1
#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/2 19:23
__Author__ = '村长'

import sys
from subprocess import PIPE,Popen

class Exceutor:
    """
    定义初始化参数与执行返回值
    """
    def __init__(self,script,res=None):
        self.script = script
        self.res = res

    def run(self):
        """
        定义运行命令
        :return:
        """
        proc = Popen(self.script,shell=True,stdout=PIPE,stdin=PIPE)
        code = proc.wait(self.res)
        txt = proc.stdout.read()
        return code,txt


if __name__ == '__main__':
    """
    脚本执行入口
    """
    CMD = sys.argv[1]
    if CMD:
        e = Exceutor(CMD)
        result = e.run()
        if result[0] is not 0:
            print("执行命令有问题")
        else:
            print(result)





#No.2



def cache(x):
    def wrapper(func):
        def inner(*args,**kwargs):
            """
            执行装饰函数之前先判断是否符合条件
            :param args:
            :param kwargs:
            :return:
            """
            if x > 5:
                return "未命中缓存"
             elif x <= 5:
                # 符合条件执行装饰函数
                ret = func(*args,**kwargs)
                print("恭喜命中")
                return ret
        return inner
    return wrapper

@cache(4)
def haha(z,y):
    return z + y

print(haha(1,2))

