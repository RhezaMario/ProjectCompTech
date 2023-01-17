import sys

sys.path.insert(0, "../..")

import Lexer
import parsers
import Interpreter

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    prog = parsers.parse(data)
    if not prog:
        raise SystemExit
    r = Interpreter.RInterpreter(prog)
    try:
        r.run()
        raise SystemExit
    except RuntimeError:
            pass
else:
    r = Interpreter.RInterpreter([])