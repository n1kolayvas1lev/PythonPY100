# TODO


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

    # todo lower
    str_ = main_str.lower()
    str_ = [i for i in str_ if i.isalpha()]
    str_ = ''.join(str_)



    dict_chars = {}
    for char in str_:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    s = sum(dict_chars.values())
    n_char = {}
    for char in dict_chars:
        #print(dict_chars[char])
        dict_chars[char] == dict_chars[char]/s

    print(dict_chars)
