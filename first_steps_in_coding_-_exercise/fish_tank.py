lenght = int(input())
wedth = int(input())
hight = int(input())
procent = float(input())
tank = lenght * wedth * hight
liters = tank * 0.001
procent_tank = procent * 0.01
needed_liters = liters * (1 - procent_tank)
print(needed_liters)