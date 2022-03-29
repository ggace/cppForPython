import ctypes
import timeit
import math

import os


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

libc = ctypes.CDLL('./cForPython.dll')
libcpp = ctypes.CDLL('./cppForPython.dll')

libc.is_prime.argtypes = [ctypes.c_int]
libc.is_prime.restype = ctypes.c_int
libcpp.is_prime_cpp.argtypes = [ctypes.c_bool]
libcpp.is_prime_cpp.restype = ctypes.c_bool

def test():
    libc.is_prime(2147483647)

def test2():
    is_prime(2147483647)
    
def test3():
    libcpp.is_prime_cpp(2147483647)



if __name__ == '__main__':  
    count = 1000
    t_c = timeit.timeit(test, number=count) # 1000번 실행에 걸리는 시간
    t_py = timeit.timeit(test2, number=count) # 1000번 실행에 걸리는 시간
    t_cpp = timeit.timeit(test3, number=count) # 1000번 실행에 걸리는 시간
    os.system("cls")
    os.system("color 02")
    print("\n" * 100)
    print(f"-- {count}번 반복 시간 --")
    print(f"c       : {t_c}")
    print(f"python  : {t_py}")
    print(f"cpp     : {t_cpp}")
    
    print("\n" * 100)