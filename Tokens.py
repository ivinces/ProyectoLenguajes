import ply.lex as lex
#import ply.yacc as yacc

reserved = {
    'byte':'BYTE',
    'short':'SHORT',
    'int':'INT',
    'long':'LONG',
    'char':'CHAR',
    'float':'FLOAT',
    'object':'OBJECT',
    'double':'DOUBLE',
    'boolean':'BOOLEAN',
    'null':'NULL',
    'List':'LIST',
    'ArrayList': 'ARRAYLIST',
    'LinkedList' : 'LINKEDLIST',
    'Queue' : 'QUEUE',
    'DoubleLinkedList' : 'DOUBLELINKEDLIST',
    'Stack' : 'STACK',
    'new' : 'NEW',
    'final':'FINAL',
    'public':'PUBLIC',
    'protected':'PROTECTED',
    'private':'PRIVATE',
    'abstract':'ABSTRACT',
    'static':'STATIC',
    'default':'DEFAULT',
    'String' : 'STRING',
}

tokens = list(reserved.values())+ ['VAR','INTEGER', 'ESPACIO',
          'PLUS', 'MINUS','TIMES','DIVIDE','MOD','OR', 'AND','XOR','NOT','CONCAT','LESSTHAN',
          'GREATTHAN','LESSTHANEQUAL', 'GREATTHANEQUAL', 'EQUAL','EQUALS', 'NEQUAL','PLUSPLUS','MINUSMINUS', 'TIMESTIMES','CONCA',
          'TIMES_ASSIGN','DIVIDE_ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN',
          'LPAREN', 'RPAREN','LCORCHETE','RCORCHETE','LLLAVE','RLLAVE','COMA','PUNTO','PUNTOCOMA',
          'DOSCOMA', 'BLOCK_COMMENT']

t_VAR=r'[a-zA-Z_][a-zA-Z0-9_]*' #Se cambio de String a Var para que en Tipo no acepte cualquier cosa.

def t_STRING(t):
    r'String'
    t.value=t.value
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LIST(t):
    r'List'
    t.value=t.value
    return t

def t_ARRAYLIST(t):
    r'ArrayList'
    t.value=t.value
    return t

def t_LINKEDLIST(t):
    r'LinkedList'
    t.value=t.value
    return t

def t_DOUBLELINKEDLIST(t):
    r'DoubleLinkedList'
    t.value=t.value
    return t

def t_QUEUE(t):
    r'Queue'
    t.value=t.value
    return t

def t_STACK(t):
    r'Stack'
    t.value=t.value
    return t

def t_BYTE(t):
    r'byte'
    t.value=t.value
    return t

def t_SHORT(t):
    r'short'
    t.value=t.value
    return t

def t_INT(t):
    r'int'
    t.value=t.value
    return t
def t_LONG(t):
    r'long'
    t.value=t.value
    return t

def t_CHAR(t):
    r'char'
    t.value=t.value
    return t

def t_FLOAT(t):
    r'float'
    t.value=t.value
    return t

def t_OBJECT(t):
    r'Object'
    t.value=t.value
    return t

def t_DOUBLE(t):
    r'double'
    t.value=t.value
    return t

def t_BOOLEAN(t):
    r'boolean'
    t.value=t.value
    return t

def t_NULL(t):
    r'NULL'
    t.value=t.value
    return t

def t_NEW(t):
    r'new'
    t.value=t.value
    return t

def t_FINAL(t):
    r'final'
    t.value=t.value
    return t

def t_PUBLIC(t):
    r'public'
    t.value=t.value
    return t

def t_PROTECTED(t):
    r'protected'
    t.value=t.value
    return t

def t_PRIVATE(t):
    r'private'
    t.value=t.value
    return t

def t_ABSTRACT(t):
    r'abstract'
    t.value=t.value
    return t

def t_STATIC(t):
    r'static'
    t.value=t.value
    return t

def t_DEFAULT(t):
    r'default'
    t.value=t.value
    return t

def t_ESPACIO(t):
    r'" "'
    t.value=t.value
    return t

t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LCORCHETE= r'\['
t_RCORCHETE= r'\]'
t_LLLAVE = r'\{'
t_RLLAVE= r'\}'
t_COMA=r'\,'
t_PUNTO= r'\.'
t_PUNTOCOMA= r'\;'
t_DOSCOMA= r'\:'
t_NOT=r'\-'
t_CONCAT=r'\+'

t_PLUS=r'\+'
t_MINUS=r'-'
t_DIVIDE=r'/'
t_TIMES=r'\*'
t_MOD=r'%'

t_OR = r'\|\|'
t_AND = '\&\&'
t_XOR='\^\^'

t_EQUAL = '=='
t_EQUALS = '='
t_NEQUAL = '!='
t_GREATTHANEQUAL = '>='
t_LESSTHANEQUAL = '<='
t_GREATTHAN = '>'
t_LESSTHAN = '<'


t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = '/='
t_MOD_ASSIGN = '\%\='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = '-='
t_AND_ASSIGN = '&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = '\^='

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_TIMESTIMES=r'\*\*'

t_ignore_LINE_COMMENT = '//.*'

def t_BLOCK_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '{}' ({}) in line {}".format(t.value[0], hex(ord(t.value[0])), t.lexer.lineno))
    t.lexer.skip(1)

lex.lex()
