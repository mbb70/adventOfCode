import sys
import hashlib

line = sys.stdin.readline().strip()
def find_match(match):
    i = 0
    found = False
    while not found:
        i += 1
        m = hashlib.md5(''.join([line, str(i)]).encode('utf-8')).hexdigest()
        found = m.startswith(match)
    return i
print("Number appended to start with 00000:", find_match('00000'))
print("Number appended to start with 000000:", find_match('000000'))

