import ply.yacc as yacc
from Tokens import *

lex.lex()

precedence=[
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'LESSTHAN', 'GREATTHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'NEW'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
]


def p_empty(p):
    """empty :"""
    pass

def p_Type(p):
    '''Type : INT
            | BOOLEAN
            | STRING
            | SHORT
            | FLOAT
            | LONG
            | DOUBLE
            | CHAR
            | BYTE
            | OBJECT
            | arraydeclaration
            | empty
            '''
    pass

def p_accessmodif(p):
    """accessmodif : PUBLIC
                    | PRIVATE
                    | PROTECTED
                    | DEFAULT
                    | empty"""
    pass

def p_finalstatvar(p):
    """finalstatvar : FINAL
                | STATIC
                | FINAL STATIC
                | empty"""
    pass

def p_declaration(p):
    """declaration : accessmodif finalstatvar Type STRING endexpression
            | accessmodif finalstatvar Type assign
            """
    pass

def p_arraydeclaration(p):
    """arraydeclaration : accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN  STRING endexpression
            | accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN STRING endexpression
            | accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression
            | accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression
            | accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN STRING endexpression
            | accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN STRING endexpression
            | accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN  assign
            | accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN assign
            | accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN assign
            | accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN assign
            | accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN assign
            | accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN assign
            """
    pass

def p_assign(p):
    '''assign : STRING EQUALS expression endexpression
            | STRING EQUALS expressionarray endexpression'''
    pass

def p_endexpression(p):
    """endexpression : PUNTOCOMA"""
    pass

def p_expression(p):
    '''expression : expression PLUS expression
           | expression MINUS expression
           | expression TIMES expression
           | expression DIVIDE expression
           | expression MOD expression
           | PLUSPLUS
           | MINUSMINUS
           | expression TIMESTIMES expression
           | TIMES_ASSIGN expression
           | MINUS_ASSIGN expression
           | PLUS_ASSIGN expression
           | DIVIDE_ASSIGN expression
           | MOD_ASSIGN expression
           | LPAREN expression RPAREN
           | INTEGER
           | empty'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[1] == '++':
        p[0]+=p[0]
    elif p[1] == '--':
        p[0]-=p[0]
    elif p[2] == '**':
        p[0] = p[1] ** p[3]
    elif p[1] == '+=':
        p[0] += p[2]
    elif p[1] == '-=':
        p[0] -= p[2]
    elif p[1] == '/=':
        p[0] /= p[2]
    elif p[1] == '*=':
        p[0] *= p[2]
    elif p[1] == '%=':
        p[0] %= p[2]
    pass

def p_expressionarray(p):
    """expressionarray : NEW LIST GREATTHAN Type LESSTHAN LPAREN RPAREN
           | NEW LINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN
           | NEW DOUBLELINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN
           | NEW QUEUE GREATTHAN Type LESSTHAN LPAREN RPAREN
           | NEW STACK GREATTHAN Type LESSTHAN LPAREN RPAREN"""
    pass

def p_error(p):
    print("Syntax error")
    pass

yacc.yacc()
