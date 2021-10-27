if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_ = [int(i) for i in list_]
    #print(list_)
    ch_l = [int(i) for i in range(len(list_)) if i % 2 == 0]
    n_ch_l = [int(i) for i in range(len(list_)) if i % 2 != 0]
    if len(ch_l) > len(n_ch_l):
        print('Чёт. больше.')
    elif len(ch_l) == len(n_ch_l):
        print('Чёт. и н/чёт одинаково.')
    else:
        print('Н/чёт. больше.')