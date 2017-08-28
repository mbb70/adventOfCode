import sys

paper, ribnon = 0, 0
for line in sys.stdin:
    l, w, h = [int(d) for d in line.split('x')]
    m = min(l*w, w*h, h*l)
    paper += 2*l*w + 2*w*h + 2*h*l + m

    ribbon += 2 * min(l+w, w+h, h+l) + l*w*h

print("Wrapping Paper Required: {} feet".format(paper))
print("Ribbon Required: {} feet".format(ribbon))

