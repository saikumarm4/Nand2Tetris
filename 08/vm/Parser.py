'''
Created on Feb 13, 2016

@author: Sai Kumar Manchala
'''
import string

class Parser(object):
    '''
    A Parser class to convert 
    Jack Intermediate code to
    Hack Assembly Language
    
    ** Arithmetic Parsing 
    '''
    PATH = None
    def __init__(self, filename, PATH):
        '''
        Constructor
        '''
        Parser.PATH = PATH
        self._filename = filename
        self._file_object = file(PATH + '\\' + filename, 'r')
        self._lines = ['call Sys.init 0']
    
    
    def get_filename(self):
        return self._filename
    
    def first_scan(self):
        """
        First scan to remove comments
        """
        
        for line in self._file_object.readlines():
            strip_line = string.strip(line)
            # Eliminating empty lines and line beginning with '//'
            if len(strip_line) == 0 or strip_line[0:2] == '//': 
                continue
            # removing whitespace and getting rid of comment
            white_space_free_line = string.rstrip(string.split(strip_line, '/')[0], ' ')
            self._lines.append(white_space_free_line)
    
    
    def print_lines(self):
        """
        Helper function to look at the comment free code
        """
        for line in self._lines:
            print line
        
    def get_line(self):
        for line in self._lines:
            yield line