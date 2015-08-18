class Registers(object):
    ERIP = 0x0 # Instruction pointer
    ERAX = 0x1 # General purpose
    ERBX = 0x2 # General purpose
    ERCX = 0x3 # Loop Counter
    ERDX = 0x4 # General purpose
    NYAN = 0x5 # General purpose
    GERD = 0x6 # Reserved for jesus
    def __init__(self, **kwargs):
        self.values = kwargs
        for reg in [Registers.ERIP, Registers.ERAX, Registers.ERBX, \
                    Registers.ERCX, Registers.ERDX, Registers.NYAN, \
                    Registers.GERD]:
            if reg not in self.values:
                self.values[reg] = 0

def is_register(s):
    return s in ['ERIP', 'ERAX', 'ERBX', 'ERCX', 'ERDX', 'NYAN', 'GERD']

def to_register(s):
    return {'ERIP': Registers.ERIP, \
            'ERAX': Registers.ERAX, \
            'ERBX': Registers.ERBX, \
            'ERCX': Registers.ERCX, \
            'ERDX': Registers.ERDX, \
            'NYAN': Registers.NYAN, \
            'GERD': Registers.GERD}[s]

def decode_literal(lit):
    prefixes = ['0x', '0b']
    if len(lit) < 2 or lit[:2] not in prefixes:
        return int(lit, 10)
    elif lit[:2] == '0x':
        return int(lit, 16)
    elif lit[:2] == '0b':
        return int(lit, 2)
    else:
        raise ValueError('Unknown base for literal: "%s"'%lit)

class VM(object):
    def __init__(self, registers=None, code=None):
        if registers:
            self.registers = registers
        else:
            self.registers = Registers()
        if code:
            self.code = code
        else:
            self.code = []
        self.stack = []

    def has_insts(self):
        return self.registers.values[Registers.ERIP] < len(self.code)

    def step(self):
        curr_inst = self.code[self.registers.values[Registers.ERIP]]
        # XXX: This is absolutely disgusting.
        try:
            inst, arg1, arg2 = curr_inst.split(' ') # binary
        except ValueError:
            try:
                inst, arg1 = curr_inst.split(' ') # unary
            except ValueError:
                inst = curr_inst.strip() # nullary
        did_jump = False
        if inst == 'ERDD':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] += val
        elif inst == 'DERV':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] = val / self.registers.values[to_register(arg2)]
        elif inst == 'MERD':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] = val % self.registers.values[to_register(arg2)]
        elif inst == 'ERND':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] &= val
        elif inst == 'ER':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] |= val
        elif inst == 'XER':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] ^= val
        elif inst == 'MERV':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[to_register(arg2)] = val
        elif inst == 'CERNJERP':
            val = 0
            cond = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            if is_register(arg2):
                cond = self.registers.values[to_register(arg2)]
            else:
                cond = decode_literal(arg2)
            if cond == 1:
                self.registers.values[Registers.ERIP] = val
                did_jump = True
        elif inst == 'SWERP':
            tmp = self.registers.values[to_register(arg1)]
            self.registers.values[to_register(arg1)] = self.registers.values[to_register(arg2)]
            self.registers.values[to_register(arg2)] = tmp
        elif inst == 'ERNC':
            self.registers.values[to_register(arg1)] += 1
        elif inst == 'DERC':
            self.registers.values[to_register(arg1)] -= 1
        elif inst == 'JERP':
            val = 0
            if is_register(arg1):
                val = self.registers.values[to_register(arg1)]
            else:
                val = decode_literal(arg1)
            self.registers.values[Registers.ERIP] = val
        elif inst == 'NERT':
            self.registers.values[to_register(arg1)] = ~self.registers.values[to_register(arg1)] 
        elif inst == 'PERP':
            self.registers.values[to_register(arg1)] = self.stack.pop()
        elif inst == 'PERSH':
            self.stack.append(self.registers.values[to_register(arg1)])
        elif inst == 'ERLYERREGSERBERLERTERERS':
            for reg in ['ERIP', 'ERAX', 'ERBX', 'ERCX', 'ERDX', 'NYAN', 'GERD']:
                self.registers.values[to_register(reg)] = 0x1337beef
        # If we didn't jump, inc ERIP (otherwise ERIP is exactly where we want it)
        if not did_jump:
            self.registers.values[Registers.ERIP] += 1

if __name__ == '__main__':
    code = """
    ERDD 1 ERAX
    DERC ERAX
    ERDD 0xff ERAX
    """
    vm = VM(code = code.strip().split('\n'))
    while vm.has_insts():
        vm.step()
    print vm.registers.values[Registers.ERAX]
