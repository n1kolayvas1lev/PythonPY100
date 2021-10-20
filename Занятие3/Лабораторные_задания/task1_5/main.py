# def f(i):
#     s = []
#     while i != 0:
#         if i > 0:
#             s.append(i)
#         i = int(input())
#     return sum(s)
#
#
# if __name__ == "__main__":
#     inp = int(input())
#     print(f(inp))


def f():
    s = []
    while True:
        i = int(input())
        if i == 0:
            break

        if i > 0:
            s.append(i)
    return sum(s)


if __name__ == "__main__":
    print(f())
