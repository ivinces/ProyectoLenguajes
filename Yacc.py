import ply.yacc as yacc
from Tokens import *
from asignar_var import *
from tkinter import *
lexer=lex.lex()

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


def p_program(p):
    """program :  declaration
                | listdeclaration
                | arraydeclaration
                | linkedlistdeclaration
                | doublelinkedlistdeclaration
                | stackdeclaration
                | queuedeclaration
        """
    pass
def p_Type(p):
    '''Type : INT
            | BOOLEAN
            | SHORT
            | FLOAT
            | LONG
            | STRING
            | DOUBLE
            | CHAR
            | BYTE
            | OBJECT
            '''
    pass

def p_Typet(p):
    '''Typet : INT
            | BOOLEAN
            | SHORT
            | FLOAT
            | LONG
            | DOUBLE
            | STRING
            | CHAR
            | BYTE
            | OBJECT
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
    """declaration : accessmodif finalstatvar Type VAR endexpression
            | accessmodif finalstatvar Type assign
            """
    pass

def p_listdeclaration(p):
    """listdeclaration : accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN VAR endexpression
            | accessmodif accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN VAR endexpression
            | accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN  listassign
            | accessmodif accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN listassign
    """
    pass

def p_listassign(p):
    '''listassign : VAR EQUALS listexpression endexpression'''
    pass

def p_listexpression(p):
    """listexpression : NEW LIST LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_arraydeclaration(p):
    """arraydeclaration : accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN VAR endexpression
            | accessmodif accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN VAR endexpression
            | accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN arrayassign
            | accessmodif accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN arrayassign
            """
    pass

def p_arrayassign(p):
    '''arrayassign : VAR EQUALS arrayexpression endexpression'''
    pass

def p_arrayexpression(p):
    """arrayexpression : NEW ARRAYLIST LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_linkedlistdeclaration(p):
    """linkedlistdeclaration : accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN linkedlistassign
                            | accessmodif accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN linkedlistassign
    """
    pass

def p_linkedlistassign(p):
    '''linkedlistassign : VAR EQUALS linkedlistexpression endexpression'''
    pass

def p_linkedlistexpression(p):
    """linkedlistexpression : NEW LINKEDLIST LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_doublelinkedlistdeclaration(p):
    """doublelinkedlistdeclaration : accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN doublelinkedlistassign
                            | accessmodif accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN doublelinkedlistassign
    """
    pass

def p_doublelinkedlistassign(p):
    '''doublelinkedlistassign : VAR EQUALS doublelinkedlistexpression endexpression'''
    pass

def p_doublelinkedlistexpression(p):
    """doublelinkedlistexpression : NEW DOUBLELINKEDLIST LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_stackdeclaration(p):
    """stackdeclaration : accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN VAR endexpression
                            | accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN stackassign
                            | accessmodif accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN stackassign
    """
    pass

def p_stackassign(p):
    '''stackassign : STRING EQUALS stackexpression endexpression'''
    pass

def p_stackexpression(p):
    """stackexpression : NEW STACK LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_queuedeclaration(p):
    """queuedeclaration : accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN  VAR endexpression
                            | accessmodif accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN  VAR endexpression
                            | accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN queueassign
                            | accessmodif accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN queueassign
    """
    pass

def p_queueassign(p):
    '''queueassign : VAR EQUALS queueexpression endexpression'''
    pass

def p_queueexpression(p):
    """queueexpression : NEW QUEUE LESSTHAN Typet GREATTHAN LPAREN RPAREN
                        | NEW LINKEDLIST LESSTHAN Typet GREATTHAN LPAREN RPAREN
        """
    pass

def p_assign(p):
    '''assign : VAR EQUALS expression endexpression'''
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

def p_empty(p):
    """empty :"""
    pass

def p_error(error):
    raise SyntaxError

parser=yacc.yacc()


def comprobar(a):
    s = a.replace(" ", "")
    try:
        parser.parse(s)
        text="Correcta"
    except SyntaxError or Exception:
        text="Incorrecta"

    return text
