import sys
import re

def part1_match(line):
    vowels = len(re.findall(r'[aeiou]', line)) >= 3
    repeaters = re.search(r'(.)\1', line)
    bad_patterns = re.search(r'ab|cd|pq|xy', line)
    return vowels and repeaters and not bad_patterns

def part2_match(line):
    repeater = re.search(r'(..).*\1', line)
    betweener = re.search(r'(.).\1', line)
    return repeater and betweener

sin = sys.stdin.readlines()
print("Part 1 Matches:", len(list(filter(part1_match, sin))))
print("Part 2 Matches:", len(list(filter(part2_match, sin))))

