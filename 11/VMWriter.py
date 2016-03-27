'''
Created on Mar 22, 2016

@author: saikumar
'''
class VMWriter:
    """
    Segments
    'argument', 'local', 'static', 'field', 'temp'
    Id_Type
    'user_class', 'int', 'char', 'boolean'
    """
    
    def __init__(self, out_file_name):
        self._out_file_name = out_file_name
        self._file_object = open(out_file_name, 'w')
    
    def write_subroutine(self, class_name, sub_name, local_var_count):
        print 'Subroutine',
        temp_buffer = 'function ' + class_name + '.' +\
                        sub_name + ' ' + str(local_var_count) + '\n'
        self.flush(temp_buffer)
    
    def write_call(self, class_name, sub_name, argument_count):
        temp_buffer = 'call ' + class_name + '.' +\
                        sub_name + ' ' + str(argument_count) + '\n'
        self.flush(temp_buffer)
    
    def write_if_goto(self, label):
        temp_buffer = 'if-goto ' + label + '\n'
        self.flush(temp_buffer)
     
    def write_goto(self, label):
        temp_buffer = 'goto ' + label + '\n'
        self.flush(temp_buffer)
        
    def write_label(self, label):
        temp_buffer = 'label ' + label + '\n'
        self.flush(temp_buffer)
        
    def write_push(self, segment, index):
        temp_buffer = 'push ' +  segment + ' ' + str(index) + '\n'
        self.flush(temp_buffer)
        
    def write_pop(self, segment, index):
        temp_buffer = 'pop ' +  segment + ' ' + str(index) + '\n'
        self.flush(temp_buffer)
    
    def write_arithmatic(self, operator, helper=None):
        temp_buffer = ""
        if operator == '+':
            temp_buffer = 'add\n'
        elif operator == '-' and helper == None:
            temp_buffer = 'sub\n'
        elif operator == '-' and helper == 'NEG':
            temp_buffer = 'neg\n'
        elif operator == '~':
            temp_buffer = "not\n"
        elif operator == '<':
            temp_buffer = "lt\n"
        elif operator == '>':
            temp_buffer = "gt\n"
        elif operator == '&':
            temp_buffer = "and\n"
        elif operator == '|':
            temp_buffer = "or\n"
        elif operator == '=':
            temp_buffer = "eq\n"
        elif operator == '/':
            temp_buffer = "call Math.divide 2\n"
        elif operator == '*':
            temp_buffer = 'call Math.multiply 2\n'
            
        self.flush(temp_buffer)
    
    def write_return(self):
        self.flush('return\n')
              
    def flush(self, temp_buffer):
        self._file_object.write(temp_buffer)
        self._file_object.flush()
    
    def writer_close(self):
        self._file_object.close()