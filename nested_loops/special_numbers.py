n = int(input())
# for s in range(1111, 10000):
#     h = str(s)
#     text1 = h[0]
#     text2 = h[1]
#     text3 = h[2]
#     text4 = h[3]
#     digit1 = int(text1)
#     digit2 = int(text2)
#     digit3 = int(text3)
#     digit4 = int(text4)
#     if digit1 == 0 or digit2 == 0 or digit3 == 0 or digit4 == 0:
#         continue
#     if n % digit1 == 0 and n % digit2 == 0 and n % digit3 == 0 and n % digit4 == 0:
#         print(s, end=" ")
# # Това е друг по-дълъг вариант, който е също верен, но е малко по-бавен за изчисляване от компютъра.
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if n % a == 0 and n % b == 0 and n % c == 0 and n % d == 0:
                    print(f"{a}{b}{c}{d}", end=" ")