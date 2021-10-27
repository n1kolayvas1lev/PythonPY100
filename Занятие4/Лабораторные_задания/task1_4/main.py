if __name__ == "__main__":
    n = int(input())
    m = int(input())
    list_ = [int(i) for i in range(n, m)]
    sa = sum(list_)/len(list_)
    n_list = [int(i) for i in range(n, m) if i > sa]
    print(n_list)
