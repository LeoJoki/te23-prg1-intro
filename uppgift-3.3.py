from math import sqrt

side_a = input("Hur lång är sida a?: ")
side_b = input("Hur lång är sida b?: ")
angle_a = input("Hur lång är vinkeln a?: ")

side_a_squared = float(side_a) ** 2
side_b_squared = float(side_b) ** 2

two_ab_cosa = 2 * float(side_a) * float(side_b) * float(angle_a)

ab_squared = float(side_a_squared) + float(side_b_squared)

side_c_squared = float(ab_squared) - float(two_ab_cosa)

side_c = float(side_c_squared) / float(side_c_squared)

print(f"sida c är {side_c}")

if side_c = side_b = side_a