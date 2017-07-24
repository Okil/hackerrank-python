n = 4
ar = [3, 2, 3, 1]

def candle(n, ar):
    result = 0
    s = max(ar)
    for i in ar:
        if i == s:
            result += 1
    return result


print(candle(n,a))
