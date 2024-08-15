import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
results = []

for i in range(1, n + 1):
    cur = data[i]
    length = len(cur)
    segment_len = (length + 2) // 3

    cur_prime = cur[:segment_len]
    rev_cur_prime = cur_prime[::-1]
    tail_rcp = rev_cur_prime[1:]
    tail_cp = cur_prime[1:]

    p1 = cur_prime + rev_cur_prime + cur_prime
    p2 = cur_prime + tail_rcp + cur_prime
    p3 = cur_prime + rev_cur_prime + tail_cp
    p4 = cur_prime + tail_rcp + tail_cp

    if cur == p1 or cur == p2 or cur == p3 or cur == p4:
        results.append("1")
    else:
        results.append("0")

sys.stdout.write("\n".join(results) + "\n")
