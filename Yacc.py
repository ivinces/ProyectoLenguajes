import ply.yacc as yacc
from Tokens import *

def p_empty(p):
    """empty :"""

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
            | accessmodif finalstatvar Type STRING EQUALS expression"""
    pass

def p_arraydeclaration(p):
    """arraydeclaration : LIST GREATTHAN Type LESSTHAN LPAREN RPAREN
            | ARRAYLIST GREATTHAN Type LESSTHAN LPAREN RPAREN
            | LINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN
            | DOUBLELINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN
            | QUEUE GREATTHAN Type LESSTHAN LPAREN RPAREN
            | STACK GREATTHAN Type LESSTHAN LPAREN RPAREN"""
    pass

def p_assign(p):
    '''assign: STRING EQUALS expression endexpression
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
           | NUMBER endexpression'''
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


yacc.yacc()
