'''
Created on Mar 15, 2016

@author: saikumar
'''

class SymbolTable:
    
    def __init__(self):
        self._class_table = []
        self._subroutine_table = []
        
        self._static_index = 0
        self._field_index = 0
        self._argument_index = 0
        self._var_index = 0
        
        self._subroutine_identifier = 0
    
    def define(self, identifier_details):
        name, id_type, kind = identifier_details[0], identifier_details[1], identifier_details[2]
        
        if kind in ['static', 'field']:
            if kind == 'static':
                self._class_table.append((name, id_type, kind, self._static_index))
                self._static_index += 1
            else:
                self._class_table.append((name, id_type, kind, self._field_index))
                self._field_index += 1
        else:
            if kind == 'var':
                self._subroutine_table.append((name, id_type, kind, self._var_index))
                self._var_index += 1
            elif kind == 'argument':
                self._subroutine_table.append((name, id_type, kind, self._argument_index))
                self._argument_index += 1
                    
    def startSubRoutine(self, identifier):
        self._subroutine_table = []
        self._subroutine_identifier = identifier
        self._argument_index = 0
        self._var_index = 0
                
    def indexOf(self, identifier):
        
        for name, dummy_type, dummy_kind, index in self._class_table:
            if name == identifier:
                return index
        
        for name, dummy_id_type, dummy_kind, index in self._subroutine_table:
            if name == identifier:
                return index
            
    def kindOf(self, identifier):
        for name, dummy_id_type, kind, dummy_id_index in self._class_table:
            if name == identifier:
                return kind
        
        for name, dummy_id_type, kind, dummy_id_index in self._subroutine_table:
            if name == identifier:
                return kind
            
    def typeOf(self, identifier):
        for name, id_type, dummy_kind, dummy_id_index in self._class_table:
            if name == identifier:
                return id_type
        
        for name, id_type, dummy_kind, dummy_id_index in self._subroutine_table:
            if name == identifier:
                return id_type
            
    def varCount(self, kind):
        if kind == 'static':
            return self._static_index
        elif kind == 'field':
            return self._field_index
        elif kind == 'argument':
            return self._argument_index
        elif kind == 'var':
            return self._var_index
    
    
    def printSymbolTables(self):
        print 'Class Symbol Table'
        for name, id_type, kind, index in self._class_table:
            print name, id_type, kind, index
        
        print '######################'
        
        print 'Subroutine Symbol Table'
        for name, id_type, kind, index in self._subroutine_table:
            print name, id_type, kind, index
