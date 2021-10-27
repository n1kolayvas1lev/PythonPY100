if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_ = [int(i) for i in list_]
    sa = sum(list_) / len(list_)
    n_list = [i - sa for i in list_]
    print(n_list)