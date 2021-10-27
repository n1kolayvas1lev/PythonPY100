if __name__ == "__main__":
    m = int(input())
    n = int(input())
    list_ = [i ** 2 for i in range(n, m) if i % 2 != 0]
    print(list_)
