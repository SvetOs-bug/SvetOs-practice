#!/usr/bin/env python3
import math

print(" Находим третью сторону треугольника")

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
angle_degrees = float(input("Введите угол между ними (в градусах): "))

angle_radians = math.radians(angle_degrees)

c_squared = a**2 + b**2 - 2 * a * b * math.cos(angle_radians)
c = math.sqrt(c_squared)

print(f"Длина третьей стороны равна: {round(c, 2)}")
input()
