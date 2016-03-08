'''
Created on Mar 7, 2016

@author: saikumar
'''
import string

from JackTokenizer import JackTokenizer
from Compilation import CompliationEngine


class JackAnalyzer(object):
    '''
    JackAnalyzer, top-level driver that sets up and invokes the other modules
    '''


    def __init__(self, file_name):
        '''
        Constructor
        '''
        self._file_name = file_name
        self._tokenizer = None
    
    def tokenize(self):
        self._tokenizer = JackTokenizer(self._file_name)
        self._tokenizer.makeCommentAndWhiteSpaceFree()
        self._tokenizer.prepare_tokens()
        print "###################################"
        compilation_engine = CompliationEngine(self._tokenizer, string.replace(self._file_name, '.jack', '.xml'))
        compilation_engine.Compile()        
    
def main():
    jack_analyzer = JackAnalyzer('C:\\Users\\saikumar\\workspace\\Nand2Tetris\\09\\Square.jack')
    jack_analyzer.tokenize()
    
    