import sys

sys.path.insert(0, "../..")

import Lexer
import parsers
import Interpreter

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    parsed = parsers.parse(data)
    if not parsed:
        raise SystemExit
    translated = Interpreter.Interpreter(parsed)
    try:
        translated.run()
        raise SystemExit
    except RuntimeError:
            pass
else:
    php = Interpreter.Interpreter([])