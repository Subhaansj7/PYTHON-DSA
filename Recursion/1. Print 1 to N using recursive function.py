

def fun(n):
    if n == 0:
        return
    else:
        fun(n-1)
        print(n)
        
fun(7)