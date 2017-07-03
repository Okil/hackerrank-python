import sys

def isSatisfiable(c1, c2, h1, h2):
    # Complete this function
    c = int((c1 + c2)/2)
    h = int((h1 + h2)/2)
    print(c)
    print(h)
    
# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)
