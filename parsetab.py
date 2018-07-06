
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftXORleftANDnonassocLESSTHANGREATTHANleftPLUSMINUSleftTIMESDIVIDEnonassocNEWrightPRIVATEPROTECTEDPUBLICABSTRACT AND AND_ASSIGN ARRAYLIST BLOCK_COMMENT BOOLEAN BYTE CHAR COMA CONCA CONCAT DEFAULT DIVIDE DIVIDE_ASSIGN DOSCOMA DOUBLE DOUBLELINKEDLIST EQUAL EQUALS ESPACIO FINAL FLOAT GREATTHAN GREATTHANEQUAL INT INTEGER LCORCHETE LESSTHAN LESSTHANEQUAL LINKEDLIST LIST LLLAVE LONG LPAREN MINUS MINUSMINUS MINUS_ASSIGN MOD MOD_ASSIGN NEQUAL NEW NOT NULL OBJECT OR OR_ASSIGN PLUS PLUSPLUS PLUS_ASSIGN PRIVATE PROTECTED PUBLIC PUNTO PUNTOCOMA QUEUE RCORCHETE RLLAVE RPAREN SHORT STACK STATIC STRING TIMES TIMESTIMES TIMES_ASSIGN XOR XOR_ASSIGNprogram :  declaration\n                | listdeclaration\n                | arraydeclaration\n                | linkedlistdeclaration\n                | doublelinkedlistdeclaration\n                | stackdeclaration\n                | queuedeclaration\n        Type : INT\n            | BOOLEAN\n            | STRING\n            | SHORT\n            | FLOAT\n            | LONG\n            | DOUBLE\n            | CHAR\n            | BYTE\n            | OBJECT\n            | arraydeclaration\n            | empty\n            accessmodif : PUBLIC\n                    | PRIVATE\n                    | PROTECTED\n                    | DEFAULT\n                    | emptyfinalstatvar : FINAL\n                | STATIC\n                | FINAL STATIC\n                | emptydeclaration : accessmodif finalstatvar Type STRING endexpression\n            | accessmodif finalstatvar Type assign\n            listdeclaration : accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN STRING endexpression\n            | accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN  listassign\n    listassign : STRING EQUALS listexpression endexpressionlistexpression : NEW LIST LESSTHAN Type GREATTHAN LPAREN RPAREN\n        arraydeclaration : accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN STRING endexpression\n            | accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN arrayassign\n            arrayassign : STRING EQUALS arrayexpression endexpressionarrayexpression : NEW ARRAYLIST LESSTHAN Type GREATTHAN LPAREN RPAREN\n        linkedlistdeclaration : accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN STRING endexpression\n                            | accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN linkedlistassign\n    linkedlistassign : STRING EQUALS linkedlistexpression endexpressionlinkedlistexpression : NEW LINKEDLIST LESSTHAN Type GREATTHAN LPAREN RPAREN\n        doublelinkedlistdeclaration : accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN STRING endexpression\n                            | accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN doublelinkedlistassign\n    doublelinkedlistassign : STRING EQUALS doublelinkedlistexpression endexpressiondoublelinkedlistexpression : NEW DOUBLELINKEDLIST LESSTHAN Type GREATTHAN LPAREN RPAREN\n        stackdeclaration : accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN STRING endexpression\n                            | accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN stackassign\n    stackassign : STRING EQUALS stackexpression endexpressionstackexpression : NEW STACK GREATTHAN Type LESSTHAN LPAREN RPAREN\n        queuedeclaration : accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN  STRING endexpression\n                            | accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN queueassign\n    queueassign : STRING EQUALS queueexpression endexpressionqueueexpression : NEW QUEUE LESSTHAN Type GREATTHAN LPAREN RPAREN\n        assign : STRING EQUALS expression endexpressionendexpression : PUNTOCOMAexpression : expression PLUS expression\n           | expression MINUS expression\n           | expression TIMES expression\n           | expression DIVIDE expression\n           | expression MOD expression\n           | PLUSPLUS\n           | MINUSMINUS\n           | expression TIMESTIMES expression\n           | TIMES_ASSIGN expression\n           | MINUS_ASSIGN expression\n           | PLUS_ASSIGN expression\n           | DIVIDE_ASSIGN expression\n           | MOD_ASSIGN expression\n           | LPAREN expression RPAREN\n           | INTEGER\n           | emptyempty :'
    
_lr_action_items = {'PUBLIC':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[10,-73,-20,-21,-22,-23,-24,10,-25,-26,-28,-27,10,10,10,10,10,10,10,10,10,10,10,10,]),'PRIVATE':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[11,-73,-20,-21,-22,-23,-24,11,-25,-26,-28,-27,11,11,11,11,11,11,11,11,11,11,11,11,]),'PROTECTED':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[12,-73,-20,-21,-22,-23,-24,12,-25,-26,-28,-27,12,12,12,12,12,12,12,12,12,12,12,12,]),'DEFAULT':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[13,-73,-20,-21,-22,-23,-24,13,-25,-26,-28,-27,13,13,13,13,13,13,13,13,13,13,13,13,]),'FINAL':([0,9,10,11,12,13,14,15,16,17,18,19,38,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,16,-20,-21,-22,-23,-24,-73,-25,-26,-28,16,-24,-27,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,]),'STATIC':([0,9,10,11,12,13,14,15,16,17,18,19,38,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,17,-20,-21,-22,-23,-24,-73,39,-26,-28,17,-24,-27,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,-73,]),'LIST':([0,9,10,11,12,13,14,15,16,17,18,39,120,],[-73,-73,-20,-21,-22,-23,-24,22,-25,-26,-28,-27,132,]),'ARRAYLIST':([0,9,10,11,12,13,14,15,16,17,18,19,38,39,40,43,44,45,46,47,48,122,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,23,-25,-26,-28,-73,-24,-27,23,-73,-73,-73,-73,-73,-73,134,-73,-73,-73,-73,-73,-73,]),'LINKEDLIST':([0,9,10,11,12,13,14,15,16,17,18,39,124,],[-73,-73,-20,-21,-22,-23,-24,24,-25,-26,-28,-27,136,]),'DOUBLELINKEDLIST':([0,9,10,11,12,13,14,15,16,17,18,39,126,],[-73,-73,-20,-21,-22,-23,-24,25,-25,-26,-28,-27,138,]),'STACK':([0,9,10,11,12,13,14,15,16,17,18,39,128,],[-73,-73,-20,-21,-22,-23,-24,26,-25,-26,-28,-27,140,]),'QUEUE':([0,9,10,11,12,13,14,15,16,17,18,39,130,],[-73,-73,-20,-21,-22,-23,-24,27,-25,-26,-28,-27,142,]),'INT':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,28,-25,-26,-28,-27,28,28,28,28,28,28,28,28,28,28,28,28,]),'BOOLEAN':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,29,-25,-26,-28,-27,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([0,9,10,11,12,13,14,15,16,17,18,20,21,28,29,30,31,32,33,34,35,36,37,38,39,43,44,45,46,47,48,51,69,70,71,72,73,74,91,109,133,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,21,-25,-26,-28,41,-10,-8,-9,-11,-12,-13,-14,-15,-16,-17,-18,-19,-27,21,21,21,21,21,21,-56,88,90,92,94,96,98,-36,-35,-37,21,21,21,21,21,21,]),'SHORT':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,30,-25,-26,-28,-27,30,30,30,30,30,30,30,30,30,30,30,30,]),'FLOAT':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,31,-25,-26,-28,-27,31,31,31,31,31,31,31,31,31,31,31,31,]),'LONG':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,32,-25,-26,-28,-27,32,32,32,32,32,32,32,32,32,32,32,32,]),'DOUBLE':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,33,-25,-26,-28,-27,33,33,33,33,33,33,33,33,33,33,33,33,]),'CHAR':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,34,-25,-26,-28,-27,34,34,34,34,34,34,34,34,34,34,34,34,]),'BYTE':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,35,-25,-26,-28,-27,35,35,35,35,35,35,35,35,35,35,35,35,]),'OBJECT':([0,9,10,11,12,13,14,15,16,17,18,39,43,44,45,46,47,48,143,144,145,146,147,148,],[-73,-73,-20,-21,-22,-23,-24,36,-25,-26,-28,-27,36,36,36,36,36,36,36,36,36,36,36,36,]),'$end':([1,2,3,4,5,6,7,8,42,49,51,75,89,91,93,95,97,99,107,109,111,113,115,117,131,133,135,137,139,141,],[0,-1,-2,-3,-4,-5,-6,-7,-30,-29,-56,-55,-32,-36,-40,-44,-48,-52,-31,-35,-39,-43,-47,-51,-33,-37,-41,-45,-49,-53,]),'GREATTHAN':([21,28,29,30,31,32,33,34,35,36,37,38,43,44,45,46,47,48,51,52,53,54,55,56,57,91,109,133,140,143,144,145,146,148,149,150,151,152,154,],[-10,-8,-9,-11,-12,-13,-14,-15,-16,-17,-18,-19,-73,-73,-73,-73,-73,-73,-56,69,70,71,72,73,74,-36,-35,-37,147,-73,-73,-73,-73,-73,155,156,157,158,160,]),'LESSTHAN':([21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,51,91,109,132,133,134,136,138,142,147,153,],[-10,43,44,45,46,47,48,-8,-9,-11,-12,-13,-14,-15,-16,-17,-18,-19,-56,-36,-35,143,-37,144,145,146,148,-73,159,]),'EQUALS':([41,88,90,92,94,96,98,],[50,108,110,112,114,116,118,]),'PUNTOCOMA':([41,50,58,59,60,61,62,63,64,65,67,68,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,98,100,101,102,103,104,105,106,119,121,123,125,127,129,167,168,169,170,171,172,],[51,-73,51,-62,-63,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,-65,-66,-67,-68,-69,51,51,51,51,51,51,-57,-58,-59,-60,-61,-64,-70,51,51,51,51,51,51,-34,-38,-42,-46,-50,-54,]),'PLUSPLUS':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[59,59,59,59,59,59,59,59,59,59,59,59,59,]),'MINUSMINUS':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[60,60,60,60,60,60,60,60,60,60,60,60,60,]),'TIMES_ASSIGN':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[61,61,61,61,61,61,61,61,61,61,61,61,61,]),'MINUS_ASSIGN':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[62,62,62,62,62,62,62,62,62,62,62,62,62,]),'PLUS_ASSIGN':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[63,63,63,63,63,63,63,63,63,63,63,63,63,]),'DIVIDE_ASSIGN':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[64,64,64,64,64,64,64,64,64,64,64,64,64,]),'MOD_ASSIGN':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[65,65,65,65,65,65,65,65,65,65,65,65,65,]),'LPAREN':([50,61,62,63,64,65,66,76,77,78,79,80,81,155,156,157,158,159,160,],[66,66,66,66,66,66,66,66,66,66,66,66,66,161,162,163,164,165,166,]),'INTEGER':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[67,67,67,67,67,67,67,67,67,67,67,67,67,]),'PLUS':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,76,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,76,76,76,76,76,76,-57,-58,-59,-60,76,76,-70,]),'MINUS':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,77,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,77,77,77,77,77,77,-57,-58,-59,-60,77,77,-70,]),'TIMES':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,78,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,78,78,78,78,78,78,78,78,-59,-60,78,78,-70,]),'DIVIDE':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,79,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,79,79,79,79,79,79,79,79,-59,-60,79,79,-70,]),'MOD':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,80,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,80,80,80,80,80,80,-57,-58,-59,-60,80,80,-70,]),'TIMESTIMES':([50,58,59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,],[-73,81,-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,81,81,81,81,81,81,-57,-58,-59,-60,81,81,-70,]),'RPAREN':([59,60,61,62,63,64,65,66,67,68,76,77,78,79,80,81,82,83,84,85,86,87,100,101,102,103,104,105,106,161,162,163,164,165,166,],[-62,-63,-73,-73,-73,-73,-73,-73,-71,-72,-73,-73,-73,-73,-73,-73,-65,-66,-67,-68,-69,106,-57,-58,-59,-60,-61,-64,-70,167,168,169,170,171,172,]),'NEW':([108,110,112,114,116,118,],[120,122,124,126,128,130,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration':([0,],[2,]),'listdeclaration':([0,],[3,]),'arraydeclaration':([0,15,43,44,45,46,47,48,143,144,145,146,147,148,],[4,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'linkedlistdeclaration':([0,],[5,]),'doublelinkedlistdeclaration':([0,],[6,]),'stackdeclaration':([0,],[7,]),'queuedeclaration':([0,],[8,]),'accessmodif':([0,15,43,44,45,46,47,48,143,144,145,146,147,148,],[9,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'empty':([0,9,15,19,43,44,45,46,47,48,50,61,62,63,64,65,66,76,77,78,79,80,81,143,144,145,146,147,148,],[14,18,38,18,38,38,38,38,38,38,68,68,68,68,68,68,68,68,68,68,68,68,68,38,38,38,38,38,38,]),'finalstatvar':([9,19,],[15,40,]),'Type':([15,43,44,45,46,47,48,143,144,145,146,147,148,],[20,52,53,54,55,56,57,149,150,151,152,153,154,]),'assign':([20,],[42,]),'endexpression':([41,58,88,90,92,94,96,98,119,121,123,125,127,129,],[49,75,107,109,111,113,115,117,131,133,135,137,139,141,]),'expression':([50,61,62,63,64,65,66,76,77,78,79,80,81,],[58,82,83,84,85,86,87,100,101,102,103,104,105,]),'listassign':([69,],[89,]),'arrayassign':([70,],[91,]),'linkedlistassign':([71,],[93,]),'doublelinkedlistassign':([72,],[95,]),'stackassign':([73,],[97,]),'queueassign':([74,],[99,]),'listexpression':([108,],[119,]),'arrayexpression':([110,],[121,]),'linkedlistexpression':([112,],[123,]),'doublelinkedlistexpression':([114,],[125,]),'stackexpression':([116,],[127,]),'queueexpression':([118,],[129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration','program',1,'p_program','Yacc.py',19),
  ('program -> listdeclaration','program',1,'p_program','Yacc.py',20),
  ('program -> arraydeclaration','program',1,'p_program','Yacc.py',21),
  ('program -> linkedlistdeclaration','program',1,'p_program','Yacc.py',22),
  ('program -> doublelinkedlistdeclaration','program',1,'p_program','Yacc.py',23),
  ('program -> stackdeclaration','program',1,'p_program','Yacc.py',24),
  ('program -> queuedeclaration','program',1,'p_program','Yacc.py',25),
  ('Type -> INT','Type',1,'p_Type','Yacc.py',30),
  ('Type -> BOOLEAN','Type',1,'p_Type','Yacc.py',31),
  ('Type -> STRING','Type',1,'p_Type','Yacc.py',32),
  ('Type -> SHORT','Type',1,'p_Type','Yacc.py',33),
  ('Type -> FLOAT','Type',1,'p_Type','Yacc.py',34),
  ('Type -> LONG','Type',1,'p_Type','Yacc.py',35),
  ('Type -> DOUBLE','Type',1,'p_Type','Yacc.py',36),
  ('Type -> CHAR','Type',1,'p_Type','Yacc.py',37),
  ('Type -> BYTE','Type',1,'p_Type','Yacc.py',38),
  ('Type -> OBJECT','Type',1,'p_Type','Yacc.py',39),
  ('Type -> arraydeclaration','Type',1,'p_Type','Yacc.py',40),
  ('Type -> empty','Type',1,'p_Type','Yacc.py',41),
  ('accessmodif -> PUBLIC','accessmodif',1,'p_accessmodif','Yacc.py',46),
  ('accessmodif -> PRIVATE','accessmodif',1,'p_accessmodif','Yacc.py',47),
  ('accessmodif -> PROTECTED','accessmodif',1,'p_accessmodif','Yacc.py',48),
  ('accessmodif -> DEFAULT','accessmodif',1,'p_accessmodif','Yacc.py',49),
  ('accessmodif -> empty','accessmodif',1,'p_accessmodif','Yacc.py',50),
  ('finalstatvar -> FINAL','finalstatvar',1,'p_finalstatvar','Yacc.py',54),
  ('finalstatvar -> STATIC','finalstatvar',1,'p_finalstatvar','Yacc.py',55),
  ('finalstatvar -> FINAL STATIC','finalstatvar',2,'p_finalstatvar','Yacc.py',56),
  ('finalstatvar -> empty','finalstatvar',1,'p_finalstatvar','Yacc.py',57),
  ('declaration -> accessmodif finalstatvar Type STRING endexpression','declaration',5,'p_declaration','Yacc.py',61),
  ('declaration -> accessmodif finalstatvar Type assign','declaration',4,'p_declaration','Yacc.py',62),
  ('listdeclaration -> accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN STRING endexpression','listdeclaration',8,'p_listdeclaration','Yacc.py',67),
  ('listdeclaration -> accessmodif finalstatvar LIST LESSTHAN Type GREATTHAN listassign','listdeclaration',7,'p_listdeclaration','Yacc.py',68),
  ('listassign -> STRING EQUALS listexpression endexpression','listassign',4,'p_listassign','Yacc.py',73),
  ('listexpression -> NEW LIST LESSTHAN Type GREATTHAN LPAREN RPAREN','listexpression',7,'p_listexpression','Yacc.py',77),
  ('arraydeclaration -> accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',82),
  ('arraydeclaration -> accessmodif finalstatvar ARRAYLIST LESSTHAN Type GREATTHAN arrayassign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',83),
  ('arrayassign -> STRING EQUALS arrayexpression endexpression','arrayassign',4,'p_arrayassign','Yacc.py',88),
  ('arrayexpression -> NEW ARRAYLIST LESSTHAN Type GREATTHAN LPAREN RPAREN','arrayexpression',7,'p_arrayexpression','Yacc.py',92),
  ('linkedlistdeclaration -> accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN STRING endexpression','linkedlistdeclaration',8,'p_linkedlistdeclaration','Yacc.py',97),
  ('linkedlistdeclaration -> accessmodif finalstatvar LINKEDLIST LESSTHAN Type GREATTHAN linkedlistassign','linkedlistdeclaration',7,'p_linkedlistdeclaration','Yacc.py',98),
  ('linkedlistassign -> STRING EQUALS linkedlistexpression endexpression','linkedlistassign',4,'p_linkedlistassign','Yacc.py',103),
  ('linkedlistexpression -> NEW LINKEDLIST LESSTHAN Type GREATTHAN LPAREN RPAREN','linkedlistexpression',7,'p_linkedlistexpression','Yacc.py',107),
  ('doublelinkedlistdeclaration -> accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN STRING endexpression','doublelinkedlistdeclaration',8,'p_doublelinkedlistdeclaration','Yacc.py',112),
  ('doublelinkedlistdeclaration -> accessmodif finalstatvar DOUBLELINKEDLIST LESSTHAN Type GREATTHAN doublelinkedlistassign','doublelinkedlistdeclaration',7,'p_doublelinkedlistdeclaration','Yacc.py',113),
  ('doublelinkedlistassign -> STRING EQUALS doublelinkedlistexpression endexpression','doublelinkedlistassign',4,'p_doublelinkedlistassign','Yacc.py',118),
  ('doublelinkedlistexpression -> NEW DOUBLELINKEDLIST LESSTHAN Type GREATTHAN LPAREN RPAREN','doublelinkedlistexpression',7,'p_doublelinkedlistexpression','Yacc.py',122),
  ('stackdeclaration -> accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN STRING endexpression','stackdeclaration',8,'p_stackdeclaration','Yacc.py',127),
  ('stackdeclaration -> accessmodif finalstatvar STACK LESSTHAN Type GREATTHAN stackassign','stackdeclaration',7,'p_stackdeclaration','Yacc.py',128),
  ('stackassign -> STRING EQUALS stackexpression endexpression','stackassign',4,'p_stackassign','Yacc.py',133),
  ('stackexpression -> NEW STACK GREATTHAN Type LESSTHAN LPAREN RPAREN','stackexpression',7,'p_stackexpression','Yacc.py',137),
  ('queuedeclaration -> accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN STRING endexpression','queuedeclaration',8,'p_queuedeclaration','Yacc.py',142),
  ('queuedeclaration -> accessmodif finalstatvar QUEUE LESSTHAN Type GREATTHAN queueassign','queuedeclaration',7,'p_queuedeclaration','Yacc.py',143),
  ('queueassign -> STRING EQUALS queueexpression endexpression','queueassign',4,'p_queueassign','Yacc.py',148),
  ('queueexpression -> NEW QUEUE LESSTHAN Type GREATTHAN LPAREN RPAREN','queueexpression',7,'p_queueexpression','Yacc.py',152),
  ('assign -> STRING EQUALS expression endexpression','assign',4,'p_assign','Yacc.py',157),
  ('endexpression -> PUNTOCOMA','endexpression',1,'p_endexpression','Yacc.py',161),
  ('expression -> expression PLUS expression','expression',3,'p_expression','Yacc.py',165),
  ('expression -> expression MINUS expression','expression',3,'p_expression','Yacc.py',166),
  ('expression -> expression TIMES expression','expression',3,'p_expression','Yacc.py',167),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','Yacc.py',168),
  ('expression -> expression MOD expression','expression',3,'p_expression','Yacc.py',169),
  ('expression -> PLUSPLUS','expression',1,'p_expression','Yacc.py',170),
  ('expression -> MINUSMINUS','expression',1,'p_expression','Yacc.py',171),
  ('expression -> expression TIMESTIMES expression','expression',3,'p_expression','Yacc.py',172),
  ('expression -> TIMES_ASSIGN expression','expression',2,'p_expression','Yacc.py',173),
  ('expression -> MINUS_ASSIGN expression','expression',2,'p_expression','Yacc.py',174),
  ('expression -> PLUS_ASSIGN expression','expression',2,'p_expression','Yacc.py',175),
  ('expression -> DIVIDE_ASSIGN expression','expression',2,'p_expression','Yacc.py',176),
  ('expression -> MOD_ASSIGN expression','expression',2,'p_expression','Yacc.py',177),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','Yacc.py',178),
  ('expression -> INTEGER','expression',1,'p_expression','Yacc.py',179),
  ('expression -> empty','expression',1,'p_expression','Yacc.py',180),
  ('empty -> <empty>','empty',0,'p_empty','Yacc.py',210),
]
