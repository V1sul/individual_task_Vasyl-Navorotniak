#Задача 3
import math

def calculate_angle(x, y):
    return math.atan2(y, x)

def compare_angles(x1, y1, x2, y2):
    angle_A = calculate_angle(x1, y1)
    angle_B = calculate_angle(x2, y2)

    if angle_A > angle_B:
        return "Відрізок ОА утворює більший кут з віссю ОХ."
    elif angle_B > angle_A:
        return "Відрізок ОВ утворює більший кут з віссю ОХ."
    else:
        return "Відрізки ОА та ОВ утворюють однаковий кут з віссю ОХ."


print(compare_angles(1, 2, 3, 4))