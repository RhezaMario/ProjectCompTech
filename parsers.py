import ply.yacc as yacc

from Lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
)

def p_program(p):
    '''program : OPEN statement_list CLOSE '''
    p[0] = p[2]

def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

# Print Statement
def p_command_print(p):
    '''command : PRINT print_list  optend
        | ECHO print_list optend
    '''
    p[0] = ('print', p[2], p[3])

def p_print_list(p):
    '''print_list : print_list CONCAT print_item
        | print_item'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_item_string(p):
    '''print_item : STRING'''
    p[0] = (p[1], None)

def p_item_expr(p):
    '''print_item : expression'''
    p[0] = ("", p[1])

# Aritmethic Expression
def p_expression_binop(p):
    '''
    expression : expression PLUS expression 
        | expression MINUS expression 
        | expression TIMES expression 
        | expression DIVIDE expression 
        | expression MODULO expression 
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_relop(p):
    '''
    comparison : expression LTE expression
        | expression GTE expression
        | expression LT expression
        | expression GT expression
        | expression ET expression
        | expression NE expression
    '''
    p[0] = ('relop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = ('grouped',p[2])

def p_command_def_id(p):
    '''command : ID EQUALS expression optend'''
    p[0] = ('def_id', p[1], p[3], p[4])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

# If Else
def p_if_statement(p):
    '''command : IF LPAREN comparison RPAREN LBRACKET statement_list RBRACKET
                    | IF LPAREN comparison RPAREN LBRACKET statement_list RBRACKET ELSE LBRACKET statement_list RBRACKET'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6], None)
    else:
        p[0] = ('if', p[3], p[6], 'else', p[10])

def p_statement_list(p):
    '''statement_list : statement_list statement 
                      | statement'''
    if len(p) == 3:
        if p[2] is not None:
            p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : command
        |
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = None

# Looping
def p_command_while(p):
    '''command : WHILE LPAREN comparison RPAREN LBRACKET statement_list RBRACKET'''
    p[0] = ('while', p[3], p[6])

# Error Handling
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

# Optional semicolon on the end of some statement
def p_optend(p):
    '''
    optend : SEMICOLON
        |
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None

#Building Parser
parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p