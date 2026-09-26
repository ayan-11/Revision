def newfunc(func):
    def wrapthis(*args,**kwargs):
        print("B4")
        res=func(*args,**kwargs)
        print(res)
        print("After")
        
    return wrapthis
@newfunc
def summ(a,b):
    result=a+b
    return result

c=summ(2,3)
print(c)