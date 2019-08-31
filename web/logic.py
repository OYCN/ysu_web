# coding:utf-8
import random
import sys

def gen_code(length=10):
    chars = '0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY!#$%&*+-=?@'
    if sys.version_info[0]==3 and sys.version_info[1]>=6:
        return ''.join(random.choices(chars, k=length))
    else:
        return ''.join([random.choice(chars) for _ in range(length)])

def fin_code(id, code):
    ''' Hex to Dec '''
    return (str(hex(int(id)))+'Z'+str(code))

if __name__=="__main__":
    code = gen_code()
    print(code)
    print(fin_code(1,code))