import sys

def hlf(r, regs, i):
    regs[r] //= 2
    i = i + 1
    return regs, i

def tpl(r, regs, i):
    regs[r] *= 3
    i = i + 1
    return regs, i

def inc(r, regs, i):
    regs[r] += 1
    i = i + 1
    return regs, i

def jmp(offset, regs, i):
    i = i + offset
    return regs, i

def jie(r, offset, regs, i):
    i = i + (1 if regs[r] % 2 else offset)
    return regs, i

def jio(r, offset, regs, i):
    i = i + (offset if regs[r] == 1 else 1)
    return regs, i

def parse_intruction(instrs):
    parsed = []
    for instr in instrs:
        name, args = instr.strip().split(' ', 1)
        args = args.split(', ')
        try:
            args[0] = int(args[0])
        except ValueError:
            pass
        if len(args) > 1:
            args[1] = int(args[1])
        parsed.append([name, args])
    return parsed

def run_program(program, i, regs):
    while i < len(program):
        instr, args = program[i]
        args = args.copy()
        args.extend([regs, i])
        regs, i = globals()[instr](*args)
    return regs

if __name__ == '__main__':
    program = parse_intruction(sys.stdin.readlines())
    regs = { 'a' : 0, 'b' : 0 }
    print('Register b when both start at 0:', run_program(program, 0, regs)['b'])
    regs = { 'a' : 1, 'b' : 0 }
    print('Register b when a starts at 1:', run_program(program, 0, regs)['b'])

