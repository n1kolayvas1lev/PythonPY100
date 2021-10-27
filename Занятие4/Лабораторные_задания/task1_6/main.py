if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_ = [int(i) for i in list_]
    s = 0
    for i in range(len(list_)):  # todo list comprehension
        if list_[i] > list_[0]:
            s += 1
    print(s)
