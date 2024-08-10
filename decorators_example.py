import functools

def message_decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            raise ValueError(f"excepted 2 arguments but provided: {len(args)}")
        print(f"Hello {args[0]} you are: {args[1]} year old")
        result = func(*args, **kwargs)
        return result
    return wrapper

@message_decor
def greet(name, age):
    return f"Good day: {name}: {age}"



# result = greet("somesh", 34)
# print(result)
# print(help(greet))
# print(greet.__name__)

###############################################################################################

# Decorators with Arguments
# Decorators can also take arguments. This requires an additional level of nesting.

def repeat_dec(num_time):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_time):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat_dec(num_time=3)
def greet(name):
    return f"Good Day: {name}"

# res = greet("somesh")
# print(res)



#How to add nested decorate
def debug(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        arg_repr = [repr(a) for a in args]
        kwarg_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(arg_repr + kwarg_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

def start_and_end_dec(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@debug
@start_and_end_dec
def say_hello(name):
    return f"Hello: {name}"


# res = say_hello("somesh")
# print(res)


####################################################################
#class decorate

class DecorClass:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"calling : {self.call_count} times")
        return self.func(*args, **kwargs)




@DecorClass
def say_hello(name):
    print(f"Hello: {name}")

say_hello("Somesh")
say_hello("Somesh")
