import ply.lex as lex
#import ply.yacc as yacc

reserved = {
    'byte':'BYTE',
    'short':'SHORT',
    'int':'INT',
    'long':'LONG',
    'char':'CHAR',
    'float':'FLOAT',
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
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'for':'FOR',
    'switch':'SWITCH',
    'case':'CASE',
    'do':'DO',
    'break':'BREAK',
    'continue':'CONTINUE',
    'return':'RETURN',
    'public':'PUBLIC',
    'protected':'PROTECTED',
    'private':'PRIVATE',
    'abstract':'ABSTRACT',
    'static':'STATIC',
    'default':'DEFAULT',
    'instanceof':'INSTANCEOF',
}

tokens = ['STRING','INTEGER',
          'PLUS', 'MINUS','TIMES','DIVIDE','MOD','OR', 'AND','XOR','NOT','CONCAT','LESSTHAN',
          'GREATTHAN','LESSTHANEQUAL', 'GREATTHANEQUAL', 'EQUAL', 'NEQUAL','PLUSPLUS','MINUSMINUS', 'TIMESTIMES','CONCA',
          'TIMES_ASSIGN','DIVIDE_ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN',
          'LPAREN', 'RPAREN','LCORCHETE','RCORCHETE','LLLAVE','RLLAVE','COMA','PUNTO','PUNTOCOMA',
          'DOSCOMA']+list(reserved.values())

t_STRING=r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
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

t_PLUS=r'+'
t_MINUS=r'-'
t_DIVIDE=r'/'
t_TIMES=r'*'
t_MOD=r'%'

t_OR = r'\|\|'
t_AND = '&&'
t_XOR='^^'

t_EQUAL = '=='
t_NEQUAL = '!='
t_GREATTHANEQUAL = '>='
t_LESSTHANEQUAL = '<='
t_GREATTHAN = '>'
t_LESSTHAN = '<'


t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = '/='
t_MOD_ASSIGN = '%='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = '-='
t_AND_ASSIGN = '&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = '\^='

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_TIMESTIMES=r'\*\*'

t_ignore_LINE_COMMENT = '//.*'

def t_BLOCK_COMMENT(self, t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '{}' ({}) in line {}".format(t.value[0], hex(ord(t.value[0])), t.lexer.lineno))
    t.lexer.skip(1)

lex.lex()
