def f(epsilon):
    s = 0
    i = 1
    while True:
        current_value = 1 / (2 ** i)
        if current_value > epsilon:
            s += current_value
            i += 1
        else:
            break
    #print(s)
    return(s)
if __name__ == "__main__":
    epsilon = 0.0001
    print(f(epsilon))
#    pass
