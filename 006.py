#实例006 斐波那契数列
#递归实现
def Fib(n):
    return 1 if n <= 2 else Fib(n-1) + Fib(n-2)
print(Fib(int(input())))    