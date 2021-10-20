def factorial(n):
    f = 1
    for i in range (1,n+1):
        f *= i
    return(f)
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
#    pass
