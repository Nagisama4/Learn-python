import time

def calculateruntime(func):
    def wrapper(*args, **kwargs):
        a = time.time()
        result = func(*args,**kwargs)
        b = time.time() - a
        print(b)
        return result
    return wrapper

@calculateruntime
def fun01():
    time.sleep(1)
    print("fun01")

@calculateruntime
def fun02():
    time.sleep(1.5)
    print("fun02")

fun01()
fun02()