'''
Created on Feb 7, 2016

@author: sai kumar manchala
'''
import string
import numpy

class Parser():
    '''
    This Class is Parser of Assembly
    Language a part of Assembler, as part of Nand2Tetris course 
    '''
    INSTRUCTIONS = {
        '0'    : '0101010',
        '1'    : '0111111',
        '-1'   : '0111010',
        'D'    : '0001100',
        'A'    : '0110000',
        '!D'   : '0001101',
        '!A'   : '0110001',
        '-D'   : '0001111',
        '-A'   : '0110011',
        'D+1'  : '0011111',
        'A+1'  : '0110111',
        'D-1'  : '0001110',
        'A-1'  : '0110010',
        'D+A'  : '0000010',
        'D-A'  : '0010011',
        'A-D'  : '0000111',
        'D&A'  : '0000000',
        'D|A'  : '0010101',
        'M'    : '1110000',
        '!M'   : '1110001',
        '-M'   : '1110011',
        'M+1'  : '1110111',
        'M-1'  : '1110010',
        'D+M'  : '1000010',
        'D-M'  : '1010011',
        'M-D'  : '1000111',
        'D&M'  : '1000000',
        'D|M'  : '1010101',
    }
    
    DESTINATION = {
        '0'   : '000',
        'M'   : '001',
        'D'   : '010',
        'MD'  : '011',
        'A'   : '100',
        'AM'  : '101',
        'AD'  : '110',
        'ADM' : '111'
    }
    
    JUMP = {
        '0'   : '000',
        'JGT' : '001',
        'JEQ' : '010',
        'JGE' : '011',
        'JLT' : '100',
        'JNE' : '101',
        'JLE' : '110',
        'JMP' : '111'
    }
    
    SYMBOLS = {
        'SP'        : 0,
        'LCL'       : 1,
        'ARG'       : 2,
        'THIS'      : 3,
        'THAT'      : 4,
        'R0'        : 0,
        'R1'        : 1,
        'R2'        : 2,
        'R3'        : 3,
        'R4'        : 4,
        'R5'        : 5,
        'R6'        : 6,
        'R7'        : 7,
        'R8'        : 8,
        'R9'        : 9,
        'R10'       : 10,
        'R11'       : 11,
        'R12'       : 12,
        'R13'       : 13,
        'R14'       : 14,
        'R15'       : 15,
        'SCREEN'    : 16384,
        'KBD'       : 24576
    }
    
    def __init__(self, filename):
        '''
        Parser construct tables filename as
        eliminates white spaces and comments 
        '''
        self._filename = filename
        self._file_object = file(filename)
        self._lines = []
    
    def first_scan(self):
        """
        First scan to get the addresses of LOOP variables
        """
        instruction_address = 0
        for line in self._file_object.readlines():
            strip_line = string.strip(line)
            # Eliminating empty lines and line beginning with '//'
            if len(strip_line) == 0 or strip_line[0:2] == '//': 
                continue
            # removing whitespace and getting rid of comment
            white_space_free_line = list(string.split(strip_line.replace(' ', ''), '/'))[0]
            if white_space_free_line[0] == '(':
                Parser.SYMBOLS[white_space_free_line[1:-1]] = instruction_address
            else:
                self._lines.append(white_space_free_line)
                instruction_address += 1 
    
    def print_lines(self):
        """
        Helper function to look at the white space
        and comment free code
        """
        for line in self._lines:
            print line      
    
    def get_instruction(self):
        """
        A generator to get the instruction binary code for
        respective assembly code
        """
        variable_address = 16
        for line in self._lines:
            if '@' in line:
                # for A instruction
                instruction = '0'
                # if @21 then its direct accessing
                if line[1:].isdigit():
                    instruction += numpy.binary_repr(int(line[1:]), 15)
                # Predefined variables
                elif line[1:] in Parser.SYMBOLS:
                    instruction += numpy.binary_repr(int(Parser.SYMBOLS[line[1:]]), 15)
                # user defined variables
                else:
                    Parser.SYMBOLS[line[1:]] = variable_address
                    instruction += numpy.binary_repr(variable_address, 15)
                    variable_address += 1
                yield instruction
            else:
                # for C instruction all the null cases are equal to '0'
                # hence initialized it with zero
                 
                dest, rest, comp, jump = '0', '0', '0', '0'
                # to separate destination and rest of the code
                dest_rest = (['0', '0'] + list(line.split('=')))  
                dest_rest.reverse()
                rest, dest = dest_rest[:2]
                
                # C Instruction fixed starting values
                instruction = '111'
                
                # from the rest to get computation and jump
                comp_jump = (['0', '0'] + list(rest.split(';'))) 
                comp_jump.reverse()
                
                # if there is no JMP instruction and else
                if len(list(rest.split(';'))) == 1:
                    comp, jump = comp_jump[0:2]
                else:
                    jump, comp = comp_jump[0:2]
                    
                instruction += Parser.INSTRUCTIONS[comp] +\
                                Parser.DESTINATION[dest] +\
                                Parser.JUMP[jump]
                yield instruction
                                
def main():
    FOLDER = "C:\Users\saikumar\workspace\Nand2Tetris\src\\"
    #list_of_files = ["Add.asm", "MaxL.asm", "RectL.asm", "PongL.asm"]
    list_of_files = ["Add.asm", "Max.asm", "Rect.asm", "Pong.asm"]
    for file_name in list_of_files:
        parser = Parser(FOLDER + file_name)
        parser.first_scan()
        hack_file = file(FOLDER + file_name.split('.')[0] + '.hack', 'w')
        for instruction in parser.get_instruction():
            hack_file.write(instruction + '\n')
        hack_file.flush()
                