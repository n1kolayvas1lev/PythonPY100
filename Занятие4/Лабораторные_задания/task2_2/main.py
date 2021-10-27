if __name__ == "__main__":
    list_ = [int(i) for i in input()]
    cond = (4 in list_ and 8 in list_) or (9 in list_)
    if cond:
        print('Yepp', cond)
    else:
        print('Nope')
