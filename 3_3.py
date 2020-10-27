import sys

def minRefills(d,m,stops):
    current_refill = 0
    total_refills = 0
    n = len(stops)
    stops = [0] + stops + [d]
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and (stops[current_refill + 1] - stops[last_refill]) <= m:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            total_refills += 1
    return total_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(minRefills(d, m, stops))

# print(minRefills(950,400,4,[200,375,550,750]))
# print(minRefills(10,3,4,[1,2,5,9]))
# print(minRefills(200,250,2,[100,150]))
