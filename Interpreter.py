import sys
import math
import random

class Interpreter:
    def __init__(self, prog):
        self.prog = prog

    def eval(self, expr):
        etype = expr[0]
        if etype == 'numeric':
            return expr[1]
        elif etype == 'blocks':
            return self.eval(expr[1])
        elif etype == 'operator':
            if expr[1] == '*':
                return self.eval(expr[2]) * self.eval(expr[3])
            elif expr[1] == '/':
                return float(self.eval(expr[2])) / self.eval(expr[3])
            elif expr[1] == '+':
                return self.eval(expr[2]) + self.eval(expr[3])
            elif expr[1] == '-':
                return self.eval(expr[2]) - self.eval(expr[3])
            elif expr[1] == '%':
                return self.eval(expr[2]) % self.eval(expr[3])
        elif etype == 'id':
            id = expr[1]
            if id in self.ids:
                return self.ids[id]
            else:
                print("UNDEFINED VARIABLE %s AT LINE %s" %(id, self.stat[self.pc]))
                raise RuntimeError

    def releval(self, expr):
        etype = expr[1]
        lhs = self.eval(expr[2])
        rhs = self.eval(expr[3])
        if etype == '==':
            return lhs == rhs
        elif etype == '!=':
            return lhs != rhs
        elif etype == '<=':
            return lhs <= rhs
        elif etype == '<':
            return lhs < rhs
        elif etype == '>=':
            return lhs >= rhs
        elif etype == '>':
            return lhs > rhs

    def assign(self, target, value):
        id = target
        self.ids[id] = self.eval(value)

    def run(self):
        self.ids = {} 
        self.error = 0 

        if self.error:
            raise RuntimeError

        for instr in self.prog:
            self.execute(instr)
            
    def execute(self, instr):
        op = instr[0]
        # PRINT 
        if op == 'print':
            plist = instr[1]
            out = ""
            for label, val in plist:
                out += label
                if val:
                    eval = self.eval(val)
                    out += str(eval)
            sys.stdout.write(out)

        # variable asg
        elif op == 'var_asg':
            target = instr[1]
            value = instr[2]
            self.assign(target, value)

        # IF 
        elif op == 'if':
            relop = instr[1]
            if (self.releval(relop)):
                for instr2 in instr[2]:
                    self.execute(instr2)
            elif instr[3] is not None:
                for instr2 in instr[4]:
                    self.execute(instr2)

        # LOOP 
        elif op == 'while':
            while self.releval(instr[1]):
                for instr2 in instr[2]:
                    self.execute(instr2)
            



    
