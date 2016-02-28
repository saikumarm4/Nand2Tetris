'''
Created on Feb 13, 2016

@author: Sai Kumar Manchala
'''
import string

class CodeWriter():
    """
    A class to write assembly code for
    each line of VM Code
    """
    PATH = None
    VM_STACK_COMMANDS = {
                         # Push Events
                         'push constant' :  '@X' + '\n'
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
                                            '@R3' + '\n' 
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
                        # Pop Events
                         'pop argument' :   '@X' + '\n'
                                            'D=A' + '\n'
                                            '@ARG' + '\n'
                                            'D=D+M' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R13' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop local' :      '@X' + '\n'
                                            'D=A' + '\n'
                                            '@LCL' + '\n'
                                            'D=D+M' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R15' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop static' :     '@SP' + '\n' +\
                                            'AM=M-1' + '\n' +\
                                            'D=M' + '\n' +\
                                            '@X' + '\n' +\
                                            'M=D' + '\n',
                         'pop this' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@R3' + '\n'
                                            'D=D+M' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R13' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop that' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@R4' + '\n'
                                            'D=D+M' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R13' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop pointer' :    '@X' + '\n'
                                            'D=A' + '\n'
                                            '@3' + '\n'
                                            'D=D+A' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R13' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                         'pop temp' :       '@X' + '\n'
                                            'D=A' + '\n'
                                            '@5' + '\n'
                                            'D=D+A' + '\n'
                                            '@R13' + '\n'
                                            'M=D' + '\n'
                                            '@SP' + '\n'
                                            'AM=M-1' + '\n'
                                            'D=M' + '\n'
                                            '@R13' + '\n'
                                            'A=M' + '\n'
                                            'M=D' + '\n',
                        
                        # Arithmetic Operations
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
                                    '@R13' + '\n'
                                    'M=D' + '\n'
                                    '@SP' + '\n'
                                    'AM=M-1' + '\n'
                                    'D=M' + '\n'
                                    '@R13' + '\n'
                                    'D=D-M' + '\n'
                                    '@SP' + '\n'
                                    'A=M' + '\n'
                                    'M=D' + '\n'
                                    '@SP' + '\n'
                                    'M=M+1' + '\n'
                                    '@R13' + '\n'
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
                                    'M=!M' + '\n',
                                    
                         # Program flow Control Commands
                         'label':   '(X)' + '\n',
                         'goto' :   '@X' + '\n' +\
                                    '0;JMP' + '\n',
                         'if-goto': '@SP' + '\n' +\
                                    'AM=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    'M=0' + '\n' +\
                                    '@X' + '\n' +\
                                    'D;JNE' + '\n',
                                    
                         # Function Calling Commands
                         
                         'function': '(X)' + '\n',
                         
                         'return' : '@LCL' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@FRAME' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@5' + '\n' +\
                                    'D=D-A' + '\n' +\
                                    'A=D' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@RETURN' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@ARG' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@ARG' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=D+1' + '\n' +\
                                    '@FRAME' + '\n' +\
                                    'AM=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@THAT' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@FRAME' + '\n' +\
                                    'AM=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@THIS' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@FRAME' + '\n' +\
                                    'AM=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@ARG' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@FRAME' + '\n' +\
                                    'AM=M-1' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@LCL' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@RETURN' + '\n' +\
                                    'A=M' + '\n' +\
                                    '0;JMP' + '\n',
                                    
                            'call': '@Return_FUNC_X' + '\n' +\
                                    'D=A' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=M+1' + '\n' +\
                                    
                                    '@LCL' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=M+1' + '\n' +\
                                    
                                    '@ARG' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=M+1' + '\n' +\
                                    
                                    '@THIS' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=M+1' + '\n' +\
                                    
                                    '@THAT' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@SP' + '\n' +\
                                    'A=M' + '\n' +\
                                    'M=D' + '\n' +\
                                    '@SP' + '\n' +\
                                    'M=M+1' + '\n' +\
                                    
                                    '@SP' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@N_ARG' + '\n' +\
                                    'D=D-A' + '\n' +\
                                    '@5' + '\n' +\
                                    'D=D-A' + '\n' +\
                                    '@ARG' + '\n' +\
                                    'M=D' + '\n' +\
                                    
                                    '@SP' + '\n' +\
                                    'D=M' + '\n' +\
                                    '@LCL' + '\n' +\
                                    'M=D' + '\n' +\
                                    
                                    '@_FUNC' + '\n' +\
                                    '0;JMP' + '\n' +\
                                    '(Return_FUNC_X)' + '\n'
                        }
    
    def __init__(self, parser = None, PATH = None, asmfilename = None):
        CodeWriter.PATH = PATH
        self._parser = parser
        self._asmfilename = asmfilename
        
        # for eq, gt, lt we have to use assembly symbols
        # which are used to set result and get back to code
        self._jump_sequence = 0
        
        self._file_object = None
        
    def set_parser(self, parser):
        self._parser = parser
    
    def set_filename(self, asmfilename):
        self._asmfilename = asmfilename
        
    def get_filename(self):
        return self._asmfilename
    
    def start_up_code(self):
        print '.asm File Path ' + CodeWriter.PATH + '\\' + self._asmfilename
        self._file_object = open(CodeWriter.PATH + '\\' + self._asmfilename, 'w')
        startup_code =  '@256' + '\n' +\
                        'D=A' + '\n' +\
                        '@SP' + '\n' +\
                        'M=D' + '\n'
        self._file_object.write(startup_code)
        
    def terminate_code(self):
        end_code = '(END)\n@END\n0;JMP\n'
        self._file_object.write(end_code)
        self._file_object.flush()
        self._file_object.close()
        
    def generate_code(self):
        """vm_file_label = string.rsplit(self._parser.get_filename(), '.')[0]
        self._file_object.write('(' + vm_file_label + ')\n')      """  

        for line in self._parser.get_line():
            # after the below step code_fragment in ['push argument', 'pop static', ...]
            if line.find('function') == -1 and line.find('call') == -1 and line.find('return') == -1:
                code_fragment = string.rsplit(line, ' ', 1)
                
                # Memory Access Instruction
                if len(code_fragment) == 2:
                    assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                    if code_fragment[0] in ['pop static', 'push static']:
                        assembly_code = string.replace(assembly_code, 'X',
                                                        self._parser.get_filename() + '.' + code_fragment[1])
                    else:
                        assembly_code = string.replace(assembly_code, 'X', code_fragment[1])
                    self._file_object.write(assembly_code)
                # Arithmetic Instruction
                elif len(code_fragment) == 1:
                    if code_fragment[0] in ['add', 'sub', 'or', 'not', 'and', 'neg']:
                        assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                        self._file_object.write(assembly_code)
                    elif code_fragment[0] in ['eq', 'gt', 'lt']:
                        assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                        assembly_code = string.replace(assembly_code, '_J', '_' + str(self._jump_sequence))
                        self._file_object.write(assembly_code)
                        self._jump_sequence += 1
            else:
                
                code_fragment = string.split(line, ' ')
                assembly_code = CodeWriter.VM_STACK_COMMANDS[code_fragment[0]]
                if code_fragment[0] not in ['return', 'call'] :
                    assembly_code = string.replace(assembly_code, 'X', code_fragment[1])
                elif code_fragment[0] == 'call':
                    assembly_code = string.replace(assembly_code, '_X', '_' + str(self._jump_sequence))
                    assembly_code = string.replace(assembly_code, '_FUNC', code_fragment[1])
                    assembly_code = string.replace(assembly_code, 'N_ARG', code_fragment[2])
                    self._jump_sequence += 1
                self._file_object.write(assembly_code)
                