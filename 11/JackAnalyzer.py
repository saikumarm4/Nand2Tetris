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
        output_filename = string.replace(self._file_name, '.jack', '.vm')
        #output_filename = 'E:\\Nand2Tetris\\nand2tetris\\projects\\test\Main.vm'
        compilation_engine = CompliationEngine(self._tokenizer, output_filename)
        compilation_engine.Compile()        
    
def main():
    jack_analyzer = JackAnalyzer('C:\\Users\\saikumar\\workspace\\Nand2Tetris\\11\\PongGame.jack')
    jack_analyzer.tokenize()
    
    