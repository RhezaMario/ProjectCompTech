import ply.lex as lex;

reserved = {
    'print' : 'PRINT',
    'echo' : 'ECHO',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

tokens = [
'ID',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'MODULO',
'EQUALS',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'LT',
'LTE',
'GT',
'GTE',
'ET',
'NE',
'CONCAT',
'SEMICOLON',
'NUMBER',
'STRING',
'OPEN',
'CLOSE'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'\%'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_ET = r'=='
t_NE = r'!='
t_CONCAT = r'\.'
t_SEMICOLON = r';'
def t_OPEN(t):
    r'<\?php'
    return t
def t_CLOSE(t):
    r'\?>'
    return t
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1].encode().decode("unicode_escape")
    return t

def t_NUMBER(t):
    r'\d+\.\d*|\d*\.\d+|\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t    

def t_ID(t):
    r'([a-zA-Z][a-zA-Z_0-9]* | \$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*(?<!"))'
    t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'
t_ignore_COMMENT = r'\//.*'

lexer = lex.lex()

lexer.input("")

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)