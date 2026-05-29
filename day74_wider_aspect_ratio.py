from math import gcd

def get_wider_aspect_ratio(dim1, dim2):
    def parse_dimension(dim):
        w, h = map(int, dim.split('x'))
        return w, h

    def reduce_ratio(w, h):
        g = gcd(w, h)
        return f"{w // g}:{h // g}"

    w1, h1 = parse_dimension(dim1)
    w2, h2 = parse_dimension(dim2)

    ratio1 = w1 / h1
    ratio2 = w2 / h2

    if ratio1 >= ratio2:
        return reduce_ratio(w1, h1)
    else:
        return reduce_ratio(w2, h2)

print(get_wider_aspect_ratio("1920x1080", "800x600"))      # 16:9
print(get_wider_aspect_ratio("1080x1350", "2048x1536"))    # 4:3
print(get_wider_aspect_ratio("640x480", "2440x1220"))      # 2:1
print(get_wider_aspect_ratio("360x640", "1080x1920"))      # 9:16
print(get_wider_aspect_ratio("3440x1440", "2048x858"))     # 43:18
print(get_wider_aspect_ratio("12345x61234", "12534x51234")) # 2089:8539