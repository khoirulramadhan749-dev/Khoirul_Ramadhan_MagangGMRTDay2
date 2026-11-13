import math
L1 = 6
L2 = 19

theta1 = float(input("Masukan sudut Servo 1: "))
theta2 = float(input("Masukan sudut Servo 2: "))

theta1 = math.radians(theta1)
theta2 = math.radians(theta2)

x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

print("hasil:")
print("X =", x, "cm")
print("Y =", y, "cm")
