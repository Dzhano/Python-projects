n = int(input())
l = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        h = 96
        for c in range(1, l + 1):
            i = 96
            h += 1
            for d in range(1, l + 1):
                i += 1
                for e in range(1, n + 1):
                    f = chr(h)
                    g = chr(i)
                    # if c == 1:
                    #     f = "a"
                    # elif c == 2:
                    #     f = "b"
                    # elif c == 3:
                    #     f = "c"
                    # elif c == 4:
                    #     f = "d"
                    # elif c == 5:
                    #     f = "e"
                    # elif c == 6:
                    #     f = "f"
                    # elif c == 7:
                    #     f = "g"
                    # elif c == 8:
                    #     f = "h"
                    # elif c == 9:
                    #     f = "i"
                    # if d == 1:
                    #     g = "a"
                    # elif d == 2:
                    #     g = "b"
                    # elif d == 3:
                    #     g = "c"
                    # elif d == 4:
                    #     g = "d"
                    # elif d == 5:
                    #     g = "e"
                    # elif d == 6:
                    #     g = "f"
                    # elif d == 7:
                    #     g = "g"
                    # elif d == 8:
                    #     g = "h"
                    # elif d == 9:
                    #     g = "i"
                #   # Това е друг по-дълъг вариант, който е също верен, но е малко по-бавен за изчисляване от компютъра.
                    if e > a and e > b:
                        print(f"{a}{b}{f}{g}{e}", end=" ")