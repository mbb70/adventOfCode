import sys
import json

js = json.loads(sys.stdin.read().strip())
def check(js,tot, keep_red):
    if type(js) is dict:
        if keep_red or 'red' not in js.values():
            for k,v in js.items():
                tot = check(v,tot, keep_red)
    elif type(js) is list:
        for v in js:
            tot = check(v,tot, keep_red)
    elif type(js) is int:
        tot += js
    return tot
print('Sum of digits:', check(js, 0, True))
print('Sum of non-red digits', check(js, 0, False))

