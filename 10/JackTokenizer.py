'''
Created on Mar 7, 2016

@author: saikumar
'''
import string
import re

import Lexical

class JackTokenizer(object):
    '''
    JackAnalyzer, top-level driver that sets up and invokes the other modules
    '''
    
    def __init__(self, file_name):
        '''
        Constructor
        '''
        self._file_name = file_name
        self._file_object = open(file_name)
        self._lines = []
        self._tokens = []
        self._current_token = None
        self._current_token_index = 0
        self._len_tokens = 0

    def split(self, line):
        tokens = []
        space_septd = line.split()
            
        for s_token in space_septd:
            tokens += re.split('(' + Lexical.SYMBOLS +  ')', s_token)
            
        return [s for s in tokens if s != '']
        
    def makeCommentAndWhiteSpaceFree(self):
        
        # Get rid of comments
        comment = False
        for line in self._file_object.readlines():
            line = string.strip(line)
            if len(line) == 0:
                continue
            elif line[0:3] == '/**' or line[0:2] == '/*':
                comment = True
                continue
            elif line[0] == '*':
                continue
            elif line[0] == '*' and line[-2:] == '*/' and comment == True:
                comment = False
                continue
            elif line[-2:] == '*/' and comment == True:
                comment = False
                continue
            elif line.find('//') != -1:
                if len(line[:line.find('//')]) == 0:
                    continue
                self._lines.append(line[:line.find('//')])
            else:
                self._lines.append(line)
    
    def printlines(self):
        for line in self._lines:
            print line
    
    def print_tokens(self):
        for idx in range(self._len_tokens):
            print self._tokens[idx]
          
    def prepare_tokens(self):
        for line in self._lines:
            self._tokens += self.split(line)
        
        self._len_tokens = len(self._tokens)
        
    def next_token(self):
        if self._current_token_index < self._len_tokens:
            token = self._tokens[self._current_token_index]
            self._current_token = token
            self._current_token_index += 1
            return token
        else:
            return 'NO_MORE_TOKENS'
        
    def expected_token(self):
        """
        useful in subroutine calls and Arrays
        """
        if self._current_token_index < self._len_tokens:
            return self._tokens[self._current_token_index]
        else:
            return 'NO_MORE_TOKENS'
        
    def token_type(self):
        if self._current_token in Lexical.SYMBOLS_LIST:
            return 'SYMBOL'
        elif self._current_token in Lexical.KEYWORDS:
            return 'KEYWORD'
        elif self._current_token.isdigit():
            return 'INT_CONST'
        elif self._current_token.find('"') != -1 or self._current_token[0] == '-':
            return 'STRING_CONST'
        else:
            return 'IDENTIFIER'
        
    def identifier(self):
        return self._current_token
    
    def symbols(self):
        return self._current_token
    
    def intval(self):
        return self._current_token
    
    def stringval(self):
        return self._current_token
        
    def keyword(self):
        return self._current_token