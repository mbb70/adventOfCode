import sys
import re

tot_chars = 0
tot_data = 0
tot_escaped = 0
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    chars = len(line)

    esc = re.sub(r'\\', r'\\\\', line)
    esc = re.sub(r'"', '\\"', esc)
    esc = '"{}"'.format(esc)

    line = line.strip('"')
    line = re.sub(r'\\x[0-9a-f][0-9a-f]', '_', line)
    line = re.sub(r'\\"', '_', line)
    line = re.sub(r'\\\\', '_', line)

    tot_chars += chars
    tot_data += len(line)
    tot_escaped += len(esc)

print("Character length minus data length:", tot_chars - tot_data)
print("Escaped length minus character length:", tot_escaped - tot_chars)

