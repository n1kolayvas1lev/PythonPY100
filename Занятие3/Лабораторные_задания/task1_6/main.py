def f(a_, b_):
    sum_ = 0
    for i in range(1, L_YEAR+1):
        sum_ += b_ * i ** INFLATION
    return sum_ - a_ * L_YEAR
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    INFLATION = 1.03
    L_YEAR = 10
    print(f(a, b))
