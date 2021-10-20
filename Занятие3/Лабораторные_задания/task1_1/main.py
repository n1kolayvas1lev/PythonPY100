def f():
    m_sum = 500
    c_sum = 0
    n = 1
    while c_sum <= m_sum:
        c_sum += n**2
        n += 1
    return(n)
if __name__ == "__main__":
    print(f())