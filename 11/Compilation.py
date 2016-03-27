'''
Created on Mar 15, 2016
<<<<<<< HEAD
@author: saikumar
=======

@author: sama0714
>>>>>>> origin/master
'''
"""
import SymbolTable
import Lexical
<<<<<<< HEAD
import VMWriter
import Compilation
import JackTokenizer
import JackAnalyzer
reload(SymbolTable), reload(VMWriter), reload(Compilation), reload(JackTokenizer), reload(JackAnalyzer)
"""
import Lexical
from SymbolTable import SymbolTable
from VMWriter import VMWriter
=======
import Compilation
import JackTokenizer
import JackAnalyzer

reload(SymbolTable), reload(Compilation), reload(JackTokenizer), reload(JackAnalyzer)
"""
import Lexical
from SymbolTable import SymbolTable
>>>>>>> origin/master

class CompliationEngine(object):
    '''
    Effects the actual compilation output. Gets its input from a
    JackTokenizer and emits its parsed structure into an output file/stream
    '''
    MAP = { '<' : "&lt;",
            '>' : "&gt;",
            '"' : "&quot;",
            '&' : "&amp;"
    }
    
    def __init__(self, tokenizer, out_file_name):
        '''
        Constructor
        '''
        self._tokenizer = tokenizer
<<<<<<< HEAD
        self._vm_writer = VMWriter(out_file_name)
        self._class_name = None
        self._symbol_table = SymbolTable()
        self._counter = 0
        self._subroutine_name = None
=======
        self._out_file_name = out_file_name
        self._out_file_object = open(out_file_name, 'w')
        self._symbol_table = SymbolTable() 
>>>>>>> origin/master
         
    def Compile(self):
        token = str(self._tokenizer.next_token())
        if token == 'class':
            self.CompileClass(token)          
<<<<<<< HEAD
    
    def CompileClass(self, token):
        """
        takes 'class' as token
        and end the compilation
        """
        self._class_name = self._tokenizer.next_token() # got the class name
        str(self._tokenizer.next_token()) # '{'
        token = self._tokenizer.next_token() # field declarations
=======
        
    def CompileClass(self, token):
        temp_buffer = '<class><keyword>' + token +\
                      '</keyword>'
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        self._out_file_object.write(temp_buffer)
        
        token = self._tokenizer.next_token()
        if token == '{':
            temp_buffer = "<symbol>" + str(token) + "</symbol>"
            self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
            
        token = self._tokenizer.next_token()
>>>>>>> origin/master
        
        # For declaring Class Level Variable
         
        while token in ['field', 'static']:
            token = self.CompileClassVarDec(token)        
        
        # Class Methods
<<<<<<< HEAD
        while token in ['function', 'method', 'constructor']:
            token = self.CompileSubroutine(token)
        
        self._vm_writer.writer_close()
        self._symbol_table.printSymbolTables()
    
    def CompileSubroutine(self, token):
        """
        Takes any among 'function', 'method', 'constructor'
        and return token after end of subroutine '}' 
        or simple next subroutine token
        """
        function_modifier = token
            
        str(self._tokenizer.next_token()) # return type
        function_name = str(self._tokenizer.next_token()) # name of function
        
        self._subroutine_name = function_name
        
        self._symbol_table.startSubRoutine(function_name)
        if function_modifier == 'method':
            self._symbol_table.define(['this', self._class_name, 'argument'])
            
        str(self._tokenizer.next_token()) # '('
        
        token = str(self._tokenizer.next_token()) # 'arguments'
        
        while token != ')':
            token = self.CompileParamList(token)
            
        str(self._tokenizer.next_token()) # '{'
        token = str(self._tokenizer.next_token()) # Statements or '}'
        
        while token == 'var':
            token = self.CompileVarDec(token)
            
        local_variables = self._symbol_table.varCount('local')
        
        # Writing Function VM
        self._vm_writer.write_subroutine(self._class_name, function_name, local_variables)
        if function_name == 'new':
            no_of_fields = self._symbol_table.varCount('field')
            self._vm_writer.write_push('constant', no_of_fields)
            self._vm_writer.write_call('Memory', 'alloc', 1)
            self._vm_writer.write_pop('pointer', 0)
        if function_modifier == 'method':
            self._vm_writer.write_push('argument', 0)
            self._vm_writer.write_pop('pointer', 0)
        """temp_buffer = ""
        while local_variables > 0:
            temp_buffer += 'push constant 0\n'
            local_variables -= 1
        
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()"""
                    
        while token != '}':
            token = self.CompileStatements(token)
             
        token = str(self._tokenizer.next_token()) # next subroutine
        return token
        
    def CompileStatements(self, token):
        if token == 'return':
            return self.CompileReturn(token)
        if token == 'do':
            return self.CompileDo(token)
        if token == 'let':
            return self.CompileLet(token)
        if token == 'while':
            return self.CompileWhile(token)
        if token == 'if':
            return self.CompileIf(token)
    
    def CompileIf(self, token):
        """
        Takes 'if' keyword and returns next statement token
        """
        self._counter += 1 # for linear label names
        str(self._tokenizer.next_token()) # '('
                
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token) # returns ')'
        
        self._vm_writer.write_arithmatic('~')
        label = self._class_name + '.' + 'if.' + str(self._counter) + '.L1'
        self._vm_writer.write_if_goto(label)
        
        str(self._tokenizer.next_token()) # '}'
        token = str(self._tokenizer.next_token())
        
        goto_label = self._class_name + '.' + 'if.' + str(self._counter) + '.L2'
        
        while token != '}':
            token = self.CompileStatements(token)
        
        self._vm_writer.write_goto(goto_label)
        self._vm_writer.write_label(label)

=======
        if token in ['function', 'method', 'constructor']:
            token = self.CompileSubroutine(token)
            
        temp_buffer = "<symbol>" + str(token) + "</symbol></class>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        self._out_file_object.close()
        
    def CompileSubroutine(self, token):        
        temp_buffer = "<subroutineDec><keyword>" + token + "</keyword>"
        if token == "constructor":
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        else:
            temp_buffer += "<keyword>" + str(self._tokenizer.next_token()) + "</keyword>"
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        # Compiling Parameter List
        token = str(self._tokenizer.next_token())
        temp_buffer = ""
        if token != ')':
            temp_buffer = "<parameterList>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()   
                     
            token = self.CompileParamList(token)
            
            temp_buffer = "</parameterList>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            temp_buffer = ""
        else:
            temp_buffer += "<parameterList> </parameterList>"
        temp_buffer += "<symbol>" + token + "</symbol>"
        temp_buffer += "<subroutineBody><symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        # Compiling variable Declaration
        token = str(self._tokenizer.next_token())
        
        if token ==  "var":
            token = self.CompileVarDec(token)
        
        # Compiling Statements
        temp_buffer = "<statements>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        while token != "}":
            token = self.CompileStatement(token)
            if token == None:
                break
        
        temp_buffer = "</statements><symbol>" + token +\
                         "</symbol></subroutineBody></subroutineDec>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token in ['function', 'method', 'constructor']:
            token = self.CompileSubroutine(token)
        return token
    
    def CompileStatement(self, token):
        if token == 'let':
            return self.CompileLet(token)
        elif token == 'do':
            return self.CompileDo(token)
        elif token == 'return':
            return self.CompileReturn(token)
        elif token == "if":
            return self.CompileIf(token)
        elif token == "while":
            return self.CompileWhile(token)
    
    def CompileWhile(self, token):
        temp_buffer = "<whileStatement><keyword>" + token + "</keyword>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token)
        print "In While", token
        temp_buffer = "<symbol>" + token + "</symbol>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol><statements>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        while token != '}':
            print token
            token = self.CompileStatement(token)
            
        temp_buffer = "</statements><symbol>" + token + "</symbol></whileStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        return token
    
    def CompileIf(self, token):
        temp_buffer = "<ifStatement><keyword>" + token + "</keyword>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token)
        temp_buffer = "<symbol>" + token + "</symbol>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol><statements>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        while token != '}':
            token = self.CompileStatement(token)
            
        temp_buffer = "</statements><symbol>" + token + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
>>>>>>> origin/master
        
        # optional else Command
        token = str(self._tokenizer.next_token())
        if token == "else":
            token = self.CompileElse(token)
<<<<<<< HEAD
            
        self._vm_writer.write_label(goto_label)
            
=======
        
        temp_buffer = "</ifStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
>>>>>>> origin/master
        return token
    
    
    def CompileElse(self, token):
<<<<<<< HEAD
        """
        Takes 'else' token and return next statement token
        """
        
        str(self._tokenizer.next_token()) # '{'
        
        token = str(self._tokenizer.next_token())
        while token != '}':
            token = self.CompileStatements(token)
=======
        temp_buffer = "<elseStatement><keyword>" + token + "</keyword>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol><statements>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        while token != '}':
            token = self.CompileStatement(token)
        
        temp_buffer = "</statements><symbol>" + token + "</symbol></elseStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
>>>>>>> origin/master
          
        token = str(self._tokenizer.next_token())
        return token
        
<<<<<<< HEAD
    def CompileWhile(self, token):
        """
        Takes 'while' token and returns next statement token
        """
        self._counter += 1 # for linear label names
        
        label = self._class_name + '.' + 'while.' + str(self._counter) + '.L1'
        self._vm_writer.write_label(label)
        
        str(self._tokenizer.next_token()) # '('
        
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token) # 'returns ')'
        
        self._vm_writer.write_arithmatic('~') # ~cond
        
        if_label = self._class_name + '.' + 'while.' + str(self._counter) + '.L2'
        self._vm_writer.write_if_goto(if_label)
        
        str(self._tokenizer.next_token()) # '{'
        
        token = str(self._tokenizer.next_token())
        while token != '}':
            token = self.CompileStatements(token)
            
        self._vm_writer.write_goto(label) # 'goto label'
        self._vm_writer.write_label(if_label) # label for next statement
        
        token = str(self._tokenizer.next_token())
        return token
    
    def CompileDo(self, token):
        identifier = str(self._tokenizer.next_token()) # identifer or class name
        
        token = str(self._tokenizer.next_token())
        class_name = identifier
        no_of_arguments = 0
        if token == ".":
            method_or_function = str(self._tokenizer.next_token())
            str(self._tokenizer.next_token()) # '('
            id_type = self._symbol_table.typeOf(identifier)
            
        else:
            class_name = self._class_name
            method_or_function = identifier
            no_of_arguments += 1
            self._vm_writer.write_push('pointer', '0')
            id_type = None
            
        token = str(self._tokenizer.next_token()) 
        
        if id_type != None:
            segment = self._symbol_table.kindOf(identifier)
            index = self._symbol_table.indexOf(identifier)
            self._vm_writer.write_push(segment, index)
            no_of_arguments += 1
            class_name = id_type
            
        no_arguments = 0
        if token != ')':
            token, no_arguments = self.CompilerExpressionList(token) # return value is ')'
        
        no_of_arguments += no_arguments
                
        self._vm_writer.write_call(class_name, method_or_function, no_of_arguments)
        str(self._tokenizer.next_token()) # ';'
        
        # 'void functions will return constant 0 which should be discarded'
        self._vm_writer.write_pop('temp', '0') 
        token = str(self._tokenizer.next_token())
        return token
    
    def CompileLet(self, token):
        """
        Function receiver 'let' and return ';'
        """
        identifier = str(self._tokenizer.next_token()) # left hand side identifier
        segment = self._symbol_table.kindOf(identifier)
        index = str(self._symbol_table.indexOf(identifier))
        
        token = str(self._tokenizer.next_token()) # = or [
        if_array = False
        if token == '[':
            if_array = True
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token) # ']'
            self._vm_writer.write_push(segment, index)
            self._vm_writer.write_arithmatic('+')
            
            # Equal Expression
            token = str(self._tokenizer.next_token())
                
=======
    def CompileReturn(self, token):
        temp_buffer = "<returnStatement><keyword>" + token + "</keyword>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token != ';':            
            token = self.CompileExpression(token)
        
        temp_buffer = "<symbol>" + token + "</symbol></returnStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        token = str(self._tokenizer.next_token())
        return token
        
    def CompileDo(self, token):
        """
        token we get here is 'do and we return next statement starting either do, while, let, if
        """
        temp_buffer = "<doStatement><keyword>" + token + "</keyword>"
        identifier = str(self._tokenizer.next_token())
        temp_buffer += "<identifier>" + identifier + "</identifier>"
        
        if self._symbol_table.kindOf(identifier) != None:
            print 'in Do'
            temp_buffer += "<identifiercategory>" + str(self._symbol_table.kindOf(identifier)) +\
                                "</identifiercategory>"
        else:
            if self._tokenizer.expected_token() == '.':
                temp_buffer += "<identifiercategory>" + 'class' +\
                            "</identifiercategory>"
            else:
                temp_buffer += "<identifiercategory>" + 'subroutine' +\
                            "</identifiercategory>"
                            
        temp_buffer += "<presently>" + 'used' + '</presently>'
        temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
            
        
        token = str(self._tokenizer.next_token())
        if token == ".":
            temp_buffer += "<symbol>" + token + "</symbol>"
            identifier = str(self._tokenizer.next_token())
            temp_buffer += "<identifier>" + identifier + "</identifier>"
            temp_buffer += "<identifiercategory>" + 'subroutine' +\
                            "</identifiercategory>"                
            temp_buffer += "<presently>" + 'used' + '</presently>'
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol><expressionList> "
        else:    
            temp_buffer += "<symbol>" + token + "</symbol><expressionList> "
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token != ')':
            token = self.CompilerExpressionList(token)
        
        temp_buffer = "</expressionList><symbol>" + token + "</symbol>"
        temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol></doStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        token = str(self._tokenizer.next_token())
        return token
        
    def CompileLet(self, token):
        temp_buffer = "<letStatement><keyword>" + token + "</keyword>"
        identifier = str(self._tokenizer.next_token())
        temp_buffer += "<identifier>" + identifier + "</identifier>"
        temp_buffer += "<identifiercategory>" + str(self._symbol_table.kindOf(identifier)) +\
                            "</identifiercategory>"
        temp_buffer += "<presently>" + 'used' + '</presently>'
        temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token == '[':
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
            temp_buffer = "<symbol>" + token + "</symbol>"
            
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
        
        # Equal Expression
        temp_buffer = "<symbol>" + token +\
                         "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
>>>>>>> origin/master
        # Right Hand Side Expression
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token)
        
<<<<<<< HEAD
        # End Statements
        if if_array:
            self._vm_writer.write_pop('temp', 0)
            self._vm_writer.write_pop('pointer', 1)
            self._vm_writer.write_push('temp', 0)
            self._vm_writer.write_pop('that', 0)
        else:
            self._vm_writer.write_pop(segment, index)
            
        token = str(self._tokenizer.next_token())
        return token
    
    def CompileReturn(self, token):
        """
        Takes 'return' token
        if simple return pushes dummy constant and returns 0
        """
        token = str(self._tokenizer.next_token()) # ';'?
        if token == ';':
            self._vm_writer.write_push('constant', '0')
        else:
            token = self.CompileExpression(token) # ';'
            
        self._vm_writer.write_return()
        return str(self._tokenizer.next_token())
    
    def CompilerExpressionList(self, token):
        no_of_argument = 1
        token =  self.CompileExpression(token) # returns ','
        
        while token == ",":
            no_of_argument += 1
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
        return token, no_of_argument
    
    def CompileExpression(self, token):
        """
        Expression 
        """
        token = self.CompileTerm(token)
        
        if token in Lexical.OP:
            operator = token
            token = str(self._tokenizer.next_token()) # Next term
            token = self.CompileTerm(token)
            self._vm_writer.write_arithmatic(operator)
        return token
    
    def CompileTerm(self, token):
        """
        Takes the term token and returns the token after the term
        """
        temp_buffer = ""
        if token.isdigit():
            self._vm_writer.write_push('constant', token)
        elif token[0] == '"':
            no_of_character = len(token)  - 2 # removing "
            self._vm_writer.write_push('constant', no_of_character)
            self._vm_writer.write_call('String', 'new', 1)
            for idx in range(1, len(token) - 1):
                self._vm_writer.write_push('constant', ord(token[idx]))
                self._vm_writer.write_call('String', 'appendChar', 2)
        elif token == 'true':
            self._vm_writer.write_push('constant', '1')
            self._vm_writer.write_arithmatic('-', 'NEG')
        elif token in ['false', 'null']:
            self._vm_writer.write_push('constant', '0')
        elif token == 'this':
            self._vm_writer.write_push('pointer', '0')
        elif token == '-':  
            return self.CompileNegOperator(token)
        elif token == "~":
            return self.CompileNotOperator(token)
        elif token == "(":
            token = str(self._tokenizer.next_token()) # Term token
            token = self.CompileExpression(token) # Returns ')'
        elif self._tokenizer.expected_token() == "[":
            
            identifier = token
            index = self._symbol_table.indexOf(identifier)
            segment = self._symbol_table.kindOf(identifier)
            self._vm_writer.write_push(segment, index)
            
            str(self._tokenizer.next_token()) # '['
            
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token) # return value is ']'
            
            self._vm_writer.write_arithmatic('+')
            self._vm_writer.write_pop('pointer', '1')
            self._vm_writer.write_push('that', '0')
            
        elif self._tokenizer.expected_token() == ".":
            identifier = token
            str(self._tokenizer.next_token()) # '.'
            method_or_function = str(self._tokenizer.next_token()) 
            
            str(self._tokenizer.next_token()) # '('
            
            token = str(self._tokenizer.next_token())
            no_of_arguments = 0
            
            class_name = identifier
            id_type = self._symbol_table.typeOf(identifier)
            print identifier, id_type
            if id_type != None:
                segment = self._symbol_table.kindOf(identifier)
                index = self._symbol_table.indexOf(identifier)
                self._vm_writer.write_push(segment, index)
                no_of_arguments += 1
                class_name = id_type
                
            no_arguments = 0
            if token != ")":
                token, no_arguments = self.CompilerExpressionList(token)
            
            no_of_arguments += no_arguments
            self._vm_writer.write_call(class_name, method_or_function, no_of_arguments)
        else:
            identifier = token
            index = self._symbol_table.indexOf(identifier)
            segment = self._symbol_table.kindOf(identifier)
            self._vm_writer.write_push(segment, index)
            
        token = str(self._tokenizer.next_token())
        return token
    
    def CompileNegOperator(self, token):
        token = str(self._tokenizer.next_token())
        token = self.CompileTerm(token)
        self._vm_writer.write_arithmatic('-', 'NEG')
        return token
    
    def CompileNotOperator(self, token):
        """
        Takes '~' as argument as return ')'
        """ 
        token = str(self._tokenizer.next_token()) # '('?
        if token != '(':
            token = self.CompileTerm(token)
        else:
            token = str(self._tokenizer.next_token()) #
            token = self.CompileExpression(token) # returns inner ')' res
            token = str(self._tokenizer.next_token())  # outer ')'
        
        self._vm_writer.write_arithmatic('~')
        return token
        
    def CompileParamList(self, token):
        """
        Takes type of the first argument of the 
        subroutine
        """
        id_type = token # type of var variable
        kind = 'argument'
        identifier = str(self._tokenizer.next_token()) # identifier name
        identifier_details = [identifier, id_type, kind]
        self._symbol_table.define(identifier_details)
        
        token = str(self._tokenizer.next_token())
        if token == ',':
=======
        # End of Statement
        temp_buffer = "<symbol>" + token +\
                         "</symbol></letStatement>"
                         
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        return token
        
    def CompileExpression(self, token):
        temp_buffer = "<expression>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self.CompileTerm(token)
        
        temp_buffer = "</expression>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        return token
    
    def CompileTerm(self, token):
        temp_buffer = "<term>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        if token.isdigit():
            temp_buffer = "<integerConstant>" + token + "</integerConstant>"
        elif token[0] == '"':
            temp_buffer = "<stringConstant>" + token + "</stringConstant>"
        elif token in ['true', 'false', 'null', 'this']:
            temp_buffer = "<keyword>" + token + "</keyword>"
        elif token == '-':
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            temp_buffer = ""
            token = str(self._tokenizer.next_token())
            token = self.CompileTerm(token)
        elif token == "~":
            return self.CompileNotOperator(token)
        elif token == "(":
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
            
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            temp_buffer = ""
        elif self._tokenizer.expected_token() == "[":
            temp_buffer = "<identifier>" + token + "</identifier>"
            temp_buffer += "<identifiercategory>" + str(self._symbol_table.kindOf(token)) +\
                            "</identifiercategory>"
            temp_buffer += "<presently>" + 'used' + '</presently>'
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(token)) + "</index>"
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
            
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            temp_buffer = ""
        elif self._tokenizer.expected_token() == ".":
            temp_buffer = "<identifier>" + token + "</identifier>"
            if str(self._symbol_table.kindOf(token)) != None:
                temp_buffer += "<identifiercategory>" + str(self._symbol_table.kindOf(token)) +\
                                "</identifiercategory>"
            else:
                temp_buffer += "<identifiercategory>" + 'class' +\
                                "</identifiercategory>"
            temp_buffer += "<presently>" + 'used' + '</presently>'
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(token)) + "</index>"
            
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
            
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
            temp_buffer += "<identifiercategory>" + 'subroutine' +\
                                "</identifiercategory>"
            temp_buffer += "<presently>" + 'used' + '</presently>'
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(token)) + "</index>"
            
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) +\
                             "</symbol><expressionList>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            token = str(self._tokenizer.next_token())
            if token != ")":
                token = self.CompilerExpressionList(token)
            
            temp_buffer = "</expressionList><symbol>" + token + "</symbol>"
        else:
            # varible name
            temp_buffer = "<identifier>" + token + "</identifier>"
            temp_buffer += "<identifiercategory>" + str(self._symbol_table.kindOf(token)) +\
                                "</identifiercategory>"   
            temp_buffer += "<presently>" + 'used' + '</presently>'
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(token)) + "</index>"
                        
        temp_buffer += "</term>"
        
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        token = str(self._tokenizer.next_token())
        if token in Lexical.OP:
            if token in ['<', '>', '"', "&"]:
                token_map = CompliationEngine.MAP[token]
                temp_buffer = "<symbol>" + token_map + "</symbol>"
            else:
                temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
            token = self.CompileTerm(token)
        return token
    
    def CompileNotOperator(self, token):
        temp_buffer = "<symbol>" + token + "</symbol>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        token = str(self._tokenizer.next_token())
        if token != '(':
            token = self.CompileTerm(token)
            temp_buffer = "</term>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            return token
        else:
            temp_buffer = "<term><symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
            
            temp_buffer = "<symbol>" + token + "</symbol></term></term>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
            return token
            
    def CompilerExpressionList(self, token):
        token =  self.CompileExpression(token)
        while token == ",":
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
            token = self.CompileExpression(token)
        return token            
    
    def CompileVarDec(self, token):
        identifier_details = []
        var_modifier = str(token)
        var_type = str(self._tokenizer.next_token())

        temp_buffer = "<varDec><keyword>" + var_modifier + "</keyword>"
        if var_type in ['int', 'boolean', 'char']:
            temp_buffer += "<keyword>" + var_type + "</keyword>"
        else:
            temp_buffer += "<identifier>" + var_type + "</identifier>"
        identifier = str(self._tokenizer.next_token())
        temp_buffer += "<identifier>" + identifier + "</identifier>"
        temp_buffer += "<identifier_category>" + 'var' + "</identifier_category>"
        temp_buffer += "<presently>" + 'defined' + "</presently>"
        
        identifier_details.append(identifier)
        identifier_details.append(var_type)
        identifier_details.append('var')
        
        self._symbol_table.define(identifier_details)
        temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
        
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self._tokenizer.next_token()
        
        while token == ',':
            temp_buffer = "<symbol>" + token + "</symbol>"
            identifier = str(self._tokenizer.next_token())
            temp_buffer += "<identifier>" + identifier + "</identifier>"
            temp_buffer += "<identifier_category>" + var_modifier + "</identifier_category>" 
            temp_buffer += "<presently>" + 'defined' + "</presently>"
            
            identifier_details = []
            identifier_details.append(identifier)
            identifier_details.append(var_type)
            identifier_details.append('var')
            
            self._symbol_table.define(identifier_details)
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
            
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
        
        temp_buffer = "<symbol>" + token + "</symbol></varDec>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self._tokenizer.next_token()
        
        if token == 'var':
            return self.CompileVarDec(token)
        
        return token
    
    def CompileParamList(self,token):
        identifier_details = []
        
        temp_buffer = "<keyword>" + token + "</keyword>"
        
        identifier = str(self._tokenizer.next_token())
        temp_buffer += "<identifier>" + identifier + "</identifier>"
        temp_buffer += "<identifier_category>" + 'argument' + "</identifier_category>"
        temp_buffer += "<presently>" + 'defined' + "</presently>"
        
        
        identifier_details.append(identifier)
        identifier_details.append(token)
        identifier_details.append('argument')
        self._symbol_table.define(identifier_details)
        
        temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token == ',':
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
>>>>>>> origin/master
            token = str(self._tokenizer.next_token())
            return self.CompileParamList(token)
        return token
    
<<<<<<< HEAD
    def CompileVarDec(self, token):
        """
        Takes either of 'field' or 'static' as token
        return next statement either 'var' or do, let, if, while 
        """
        id_type = str(self._tokenizer.next_token()) # type of var variable
        kind = 'local'
        identifier = str(self._tokenizer.next_token()) # identifier name
        identifier_details = [identifier, id_type, kind]
        self._symbol_table.define(identifier_details)
        token = str(self._tokenizer.next_token()) # ',' or ';
        
        while token == ',':
            identifier_details = []
            identifier = str(self._tokenizer.next_token()) # identifier name
            identifier_details = [identifier, id_type, kind]
            self._symbol_table.define(identifier_details)
            token = str(self._tokenizer.next_token()) # ',' or ';
            
        return str(self._tokenizer.next_token())
    
    def CompileClassVarDec(self, token):
        class_var_modifer = str(token) # 'field' or 'static'
        
        # primitive or user defined class
        class_var_type = str(self._tokenizer.next_token()) 
        identifier = str(self._tokenizer.next_token())
        
        identifier_details = [identifier, class_var_type, class_var_modifer]
        self._symbol_table.define(identifier_details)
=======
    def CompileClassVarDec(self, token):
        identifier_details = []
        class_var_modifier = str(token)
        class_var_type = str(self._tokenizer.next_token())

        temp_buffer = "<classVarDec><keyword>" + class_var_modifier + "</keyword>"
        if class_var_type in ['int', 'boolean', 'char']:
            temp_buffer += "<keyword>" + class_var_type + "</keyword>"
        else:
            temp_buffer += "<identifier>" + class_var_type + "</identifier>"
            
        identifier = str(self._tokenizer.next_token())
        temp_buffer += "<identifier>" + identifier + "</identifier>"
        temp_buffer += "<identifier_category>" + class_var_modifier + "</identifier_category>"
        temp_buffer += "<presently>" + 'defined' + "</presently>"
        
        identifier_details.append(identifier)
        identifier_details.append(class_var_type)
        if class_var_modifier == 'static':
            identifier_details.append('static')
        else:
            identifier_details.append('field')
        
        self._symbol_table.define(identifier_details)
        temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
>>>>>>> origin/master
        
        token = self._tokenizer.next_token()
        
        while token == ',':
<<<<<<< HEAD
            identifier =  str(self._tokenizer.next_token())
            identifier_details = [identifier, class_var_type, class_var_modifer]
            self._symbol_table.define(identifier_details)
            token = str(self._tokenizer.next_token())
        
=======
            temp_buffer = "<symbol>" + token + "</symbol>"
            identifier = str(self._tokenizer.next_token())
            temp_buffer += "<identifier>" + identifier + "</identifier>"
            temp_buffer += "<identifier_category>" + class_var_modifier + "</identifier_category>" 
            temp_buffer += "<presently>" + 'defined' + "</presently>"
            
            identifier_details = []
            identifier_details.append(identifier)
            identifier_details.append(class_var_type)
            if class_var_modifier == 'static':
                identifier_details.append('static')
            else:
                identifier_details.append('field')
            
            self._symbol_table.define(identifier_details)
            
            temp_buffer += "<index>" + str(self._symbol_table.indexOf(identifier)) + "</index>"           
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
        
        temp_buffer = "<symbol>" + token + "</symbol></classVarDec>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
>>>>>>> origin/master
        token = self._tokenizer.next_token()
        
        if token in ['field', 'static']:
            return self.CompileClassVarDec(token)
        
<<<<<<< HEAD
        return token  
=======
        return token 
>>>>>>> origin/master
