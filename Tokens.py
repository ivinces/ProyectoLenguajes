import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'ArrayList': 'ARRAYLIST',
    'LinkedList' : 'LINKEDLIST',
    'Queue' : 'QUEUE',
    'DoubleLinkedList' : 'DOUBLELINKEDLIST',
    'Stack' : 'STACK',
    'new' : 'NEW'
}

tokens = ['STRING','INTEGER',
          'PLUS', 'MINUS','TIMES','DIVIDE','MODULO','OR', 'AND','XOR','LOR','LAND','NOT','MENOR',
          'MAYOR','MENORIGUAL', 'MAYORIGUAL', 'EQUAL', 'NEQUAL','INCRE','DECRE','CONCA',
          'LPAREN', 'RPAREN','LCORCHETE','RCORCHETE','LLLAVE','RLLAVE','COMA','PUNTO','PUNTOCOMA',
          'DOSCOMA']+list(reserved.values())

t_STRING=r'[a-zA-Z_][a-zA-Z0-9_]*'

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
