class Runnable:
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        def chained_func(*args, **kwargs):
            # 其他函数使用这个函数的结果
            return other(self.func(*args, **kwargs))

        return Runnable(chained_func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def add_five(x):
    return x + 5


def multiply_by_two(x):
    return x * 2


# 使用 Runnable 包装这些函数
add_five = Runnable(add_five)
multiply_by_two = Runnable(multiply_by_two)

# 使用对象方法运行它们
chain = add_five.__or__(multiply_by_two)
print(chain(3))  # (3 + 5) * 2 = 16
# -> 16

# 将可运行的函数链接在一起
chain = add_five | multiply_by_two

# 调用链
print(chain(3))  # (3 + 5) * 2 = 16
# -> 16

from langchain_core.runnables import RunnableLambda

# 使用 RunnableLambda 包装这些函数
add_five = RunnableLambda(add_five)
multiply_by_two = RunnableLambda(multiply_by_two)

# 将可运行的函数链接在一起
chain = add_five | multiply_by_two

# 调用链
print(chain.invoke(3))
# -> 16
