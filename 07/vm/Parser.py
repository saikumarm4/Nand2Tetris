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
    
    def __init__(self, filename):
        '''
        Constructor
        '''
        self._filename = filename
        self._file_object = file(filename, 'r')
        self._lines = []
    
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
            white_space_free_line = list(string.split(strip_line, '/'))[0]
            self._lines.append(white_space_free_line)
    
    def get_filename(self):
        return string.rsplit(self._filename,'\\', 1)[1]
    
    def print_lines(self):
        """
        Helper function to look at the comment free code
        """
        for line in self._lines:
            print line
        
    def get_line(self):
        for line in self._lines:
            yield line