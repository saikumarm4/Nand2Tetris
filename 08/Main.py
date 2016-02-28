'''
Created on Feb 13, 2016

@author: saikumar
'''

from vm.Parser import Parser
from vm.CodeWriter import CodeWriter

import os
import string

class Main(object):
    
    def __init__(self):
        pass
    
    def run(self):
        PATH = "E:\\Nand2Tetris\\nand2tetris\\projects\\08\\FunctionCalls\\FibonacciElement"
        PATH = os.path.abspath(PATH)
        if os.path.isdir(PATH):
            file_name = string.rsplit(PATH, '\\', 1)[1]
            code_writer = CodeWriter(PATH=PATH)
            print 'The path is directory ' + PATH
            code_writer.set_filename(file_name + '.asm')
            code_writer.start_up_code()
            vm_files =[f for f in os.listdir(PATH) if f.find('.vm') > 0 ]
            if 'Sys.vm' in vm_files:
                sysindex = vm_files.index('Sys.vm')
                vm_files[0], vm_files[sysindex] = vm_files[sysindex], vm_files[0]
            for file_name in vm_files:
                print file_name
                parser = Parser(file_name, PATH)
                parser.first_scan()
                code_writer.set_parser(parser)
                code_writer.generate_code()
            code_writer.terminate_code()
        else:
            print 'The path is file ' + PATH
            PATH, file_name = string.rsplit(PATH, '\\', 1)
            parser = Parser(file_name, PATH)
            parser.first_scan()
            code_writer = CodeWriter(PATH=PATH)
            code_writer.set_parser(parser)
            code_writer.set_filename(string.rsplit(file_name, '.', 1)[0] + '.asm')
            code_writer.start_up_code()
            code_writer.generate_code()
            code_writer.terminate_code()

def test():
    main = Main()
    main.run()