'''
Created on Feb 13, 2016

@author: saikumar
'''

from vm.Parser import Parser
from vm.CodeWriter import CodeWriter

class Main(object):
    
    def __init__(self):
        pass
    
    def run(self):
        FOLDER = "C:\Users\saikumar\workspace\Nand2Tetris\\07\\"
        files = ['SimpleAdd.vm', 'StackTest.vm', 
                 'BasicTest.vm', 'PointerTest.vm', 'StaticTest.vm']
        for file_name in files:
            file_name = FOLDER + file_name
            parser = Parser(file_name)
            parser.first_scan()
            code_writer = CodeWriter(parser)
            code_writer.generate_code()
        

def test():
    main = Main()
    main.run()