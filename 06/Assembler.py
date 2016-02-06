'''
Created on Feb 6, 2016

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
    
    def __init__(self, filename):
        '''
        Parser construct tables filename as
        eliminates white spaces and comments 
        '''
        self._filename = filename
        self._file_object = file(filename)
        self._lines = []
        for line in self._file_object.readlines():
            strip_line = string.strip(line)
            # Eliminating empty lines and line beginning with '//'
            if len(strip_line) == 0 or strip_line[0:2] == '//': 
                continue
            # removing whitespace and getting rid of comment
            self._lines.append(string.split(strip_line.replace(' ', ''), '/')[0]) 
    
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
        for line in self._lines:
            if '@' in line:
                # for A instruction 
                yield "0" +\
                    numpy.binary_repr(int(string.strip(line[1:])), 15)
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
    list_of_files = ['Add.asm', 'MaxL.asm', 'PongL.asm', 'RectL.asm']
    # parser.print_lines()
    for file_name in list_of_files:
        parser = Parser(FOLDER + file_name)
        hack_file = file(FOLDER + file_name.split('.')[0] + '.hack', 'w')
        for instruction in parser.get_instruction():
            hack_file.write(instruction + '\n')
                