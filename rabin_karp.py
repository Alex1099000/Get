def code(c):
    return ord(c) - ord('a') + 1

def poly_hash(s):
    b = 91
    h = [0]
    p = 1
    for c in s:
        h.append(((h[-1] * b) % m + code(c)) % m)
        p = (p * b) % m
    return (h, p)

m = 100

if __name__ == "__main__":
    k=0
    s = input()
    t = input()
    s_hash, p = poly_hash(s)
    s_hash = s_hash[-1]
    h, _ = poly_hash(t)
    pos = []
    for l in range(len(t) - len(s) + 1):
        r = l + len(s)
        if s_hash == (h[r] - (h[l] * p) % m) % m:
            pos.append(str(l))
            k+=1
    if k==0:
        print("-1")
    else:
        print(*pos)
