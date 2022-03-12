n = int(input())
array = list(map(int, input().split()))
new_n = int(n ** 0.5)
new_array = []
result = []

if n != new_n ** 2:
    new_n += 1
    for _ in range(new_n ** 2 - n):
        array.append(0)

for i in range(new_n):
    m = max(array[i * new_n:(i + 1) * new_n])
    new_array.append(m)

k = int(input())

for j in range(k):
    command = input().split(" ")

    if command[0] == "upd":
        i = int(command[1])
        val = int(command[2])
        array[i] = val
        piece_index = i // new_n

        if val < new_array[piece_index] - 1:
            m = max(array[piece_index * new_n:(piece_index + 1) * new_n])
            new_array[piece_index] = m
        else:
            new_array[piece_index] = val

    elif command[0] == "max":
        l = int(command[1])
        r = int(command[2])

        new_l = l // new_n
        new_r = r // new_n

        if new_r - new_l < 2:
            m = max(array[l:r + 1])
        else:
            m = max(
                max(new_array[new_l + 1:new_r]),
                max(array[l:(new_l + 1) * new_n]),
                max(array[new_r * new_n:r + 1])
            )

        result.append(m)


print(*result)



