'''
Created on Feb 13, 2016

@author: Sai Kumar Manchala
'''
import re
import string

class CodeWriter():
    """
    A class to write assembly code for
    each line of VM Code
    """
    VM_STACK_COMMANDS = {'push constant' :  '@X' + '\n'
                                            'D=A' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push argument' :  '@X' + '\n'
                                            'D=A' + '\n'
                                            '@ARG' + '\n'
                                            'A=D+M' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push local' :     '@X' + '\n'
                                            'D=A' + '\n'
                                            '@LCL' + '\n'
                                            'A=D+M' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push static' :    '@X' + '\n'
                                            'D=A' + '\n'
                                            '@16' + '\n'
                                            'A=D+A' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push this' :      '@X' + '\n'
                                            'D=A' + '\n'
                                            '@THIS' + '\n'
                                            'A=D+M' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push that' :      '@X' + '\n'
                                            'D=A' + '\n'
                                            '@THAT' + '\n'
                                            'A=D+M' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'push pointer' :   '@X' + '\n'
                                            'D=A' + '\n'
                                            # R3 is base address of pointer
                                            '@3' + '\n' 
                                            'A=D+A' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n', 
                         'push temp' :      '@X' + '\n'
                                            'D=A' + '\n'
                                            '@5' + '\n'
                                            'A=D+A' + '\n'
                                            'D=M' + '\n'
                                            '@SP' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'M=M+1' + '\n',
                         'pop argument' :   '@X' + '\n'
                                            'D=A' + '\n'
                                            '@ARG' + '\n'
                                            'D=D+M' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop local' :      '@X' + '\n'
                                            'D=A' + '\n'
                                            '@LCL' + '\n'
                                            'D=D+M' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop static' :     '@X' + '\n'
                                            'D=A' + '\n'
                                            '@16' + '\n'
                                            'D=D+A' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop this' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@R3' + '\n'
                                            'D=D+M' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop that' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@R4' + '\n'
                                            'D=D+M' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop pointer' :    '@X' + '\n'
                                            'D=A' + '\n'
                                            '@3' + '\n'
                                            'D=D+A' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop temp' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@5' + '\n'
                                            'D=D+A' + '\n'
                                            '@R5' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R5' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'add' :    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'M=D+M' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',                                    
                         'sub' :    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@R5' + '\n'
                                    'M=D' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    '@R5' + '\n'
                                    'D=D-M' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=D' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n'
                                    '@R5' + '\n'
                                    'M=0' + '\n',
                         'neg' :    '@32767' + '\n'
                                    'D=A' + '\n'
                                    '@SP' + '\n'
                                    'A=M-1' + '\n'
                                    'M=D-M' + '\n'
                                    'M=M+1' + '\n',
                          'eq' :    '@RUN_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(TRUE_J)' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=-1' + '\n'
                                    '@EQ_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(RUN_J)' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=D-M' + '\n'
                                    'M=0' + '\n'
                                    '@TRUE_J' + '\n'
                                    'D;JEQ' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=0' + '\n'
                                    '(EQ_J)' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',
                         'gt' :     '@RUN_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(TRUE_J)' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=-1' + '\n'
                                    '@EQ_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(RUN_J)' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=D-M' + '\n'
                                    'M=0' + '\n'
                                    '@TRUE_J' + '\n'
                                    'D;JLT' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=0' + '\n'
                                    '(EQ_J)' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',
                         'lt' :     '@RUN_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(TRUE_J)' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=-1' + '\n'
                                    '@EQ_J' + '\n'
                                    '0;JMP' + '\n'
                                    '(RUN_J)' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=D-M' + '\n'
                                    'M=0' + '\n'
                                    '@TRUE_J' + '\n'
                                    'D;JGT' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=0' + '\n'
                                    '(EQ_J)' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',
                         'and' :    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'M=D&M' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',
                         'or' :     '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    'M=0' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'M=D|M' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n',
                         'not' :    '@SP' + '\n'
                                    'A=M-1' + '\n'
                                    'M=!M' + '\n'
                        }
    
    def __init__(self, parser):
        self._parser = parser
    
    def generate_code(self):
        FOLDER = "C:\Users\saikumar\workspace\Nand2Tetris\\07\\"
        file_name = string.rsplit(self._parser.get_filename(), '.', 1)[0]
        file_object = open(FOLDER + file_name + '.asm', 'w')
        
        # for eq, gt, lt we have to use control flow
        # once it sets required result back to stack
         
        jump_sequence = 0
        
        for line in self._parser.get_line():
            code_fragment = string.rsplit(line, ' ', 1)
            
            # Memory Access Instruction
            if len(code_fragment) == 2: 
                assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                assembly_code = string.replace(assembly_code, 'X', code_fragment[1])
                file_object.write(assembly_code)
            elif len(code_fragment) == 1:
                if code_fragment[0] in ['add', 'sub', 'or', 'not', 'and', 'neg']:
                    assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                    file_object.write(assembly_code)
                elif code_fragment[0] in ['eq', 'gt', 'lt']:
                    assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                    assembly_code = string.replace(assembly_code, '_J', '_' + str(jump_sequence))
                    file_object.write(assembly_code)
                    jump_sequence += 1
                    
        file_object.write('(END)\n' +\
                           '@END\n' +\
                           '0;JMP'
                         )