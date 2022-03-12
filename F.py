def intersect(x1, y1, x2, y2, xm, ym):
    b_1 = x1 - x2
    a_1 = y2 - y1
    c_1 = - a_1 * x1 - b_1 * y1

    b_2 = -xm
    a_2 = ym
    c_2 = 0

    delta = a_1 * b_2 - a_2 * b_1

    if delta:
        delta_x = -c_1 * b_2 + c_2 * b_1
        delta_y = -c_2 * a_1 + c_1 * a_2

        x = round(delta_x / delta, 5)
        y = round(delta_y / delta, 5)

        if (x, y) == (x1, y1) or (x, y) == (x2, y2):
            if min(0, xm) <= x <= max(0, xm) and min(0, ym) <= y <= max(0, ym):
                return 0.5

        elif min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            if min(0, xm) <= x <= max(0, xm) and min(0, ym) <= y <= max(0, ym):
                return 1

        return 0

    else:
        return 0



n = int(input())
x_i = []
y_i = []
intersects = 0

for i in range(n):
    x, y = map(float, input().split())
    x_i.append(x)
    y_i.append(y)

x_m, y_m = map(float, input().split())

for i in range(n):
    inter = intersect(x_i[i - 1], y_i[i - 1], x_i[i], y_i[i], x_m, y_m)
    intersects += inter

if intersects == 1:
    print("YES")

else:
    print("NO")



