'''
Created on Mar 7, 2016

@author: saikumar
'''
SYMBOLS = "{|}|\(|\)|\[|\]|\.|,|;|\+|-|\*|/|&|\||<|>|=|~"

KEYWORDS = ['class', 'method', 'function', 'constructor', 
            'int', 'boolean', 'char', 'void', 
            'var', 'static', 'field', 'let', 
            'do', 'if', 'else', 'while', 
            'return', 'true', 'false', 'null', 
            'this']

TOKEN_TYPE =  { 
                'KEYWORD'       : 0,
                'SYMBOL'        : 1, 
                'IDENTIFIER'    : 2, 
                'INT_CONST'     : 3, 
                'STRING_CONST'  : 4
            }

SYMBOLS_LIST = ['{', "}", '(', ')', 
                '[', ']', '.', ',', ';',
                '+', '-', '/', '&', '|', 
                '<', '>', '=', '~'
            ]

OP = ['+', '-', '*', '/', '&', 
      '|', '<', '>', '=' ]
