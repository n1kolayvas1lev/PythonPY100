def f(n):
    s = []
    for i in range(1, n+1):
        if n % i == 0:
            s.append(i)

    return s  # (s) -> (s, )


if __name__ == "__main__":
    n = int(input())
    print(f(n))
