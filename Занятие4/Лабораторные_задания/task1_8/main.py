if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_ = [int(i) for i in list_]
    n_list = [i ** 3 if i >= 0 else 0 for i in list_]
    print(n_list)