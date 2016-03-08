'''
Created on Mar 7, 2016

@author: saikumar
'''
"""
import Lexical
import Compilation
import JackTokenizer
import JackAnalyzer
reload(Compilation), reload(JackTokenizer), reload(JackAnalyzer)
"""
import Lexical

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
        self._out_file_name = out_file_name
        self._out_file_object = open(out_file_name, 'w')
         
    def Compile(self):
        token = str(self._tokenizer.next_token())
        if token == 'class':
            self.CompileClass(token)          
        
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
        
        # For declaring Class Level Variable
         
        while token in ['field', 'static']:
            token = self.CompileClassVarDec(token)        
        
        # Class Methods
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
        
        # optional else Command
        token = str(self._tokenizer.next_token())
        if token == "else":
            token = self.CompileElse(token)
        
        temp_buffer = "</ifStatement>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        return token
    
    
    def CompileElse(self, token):
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
          
        token = str(self._tokenizer.next_token())
        return token
        
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
        temp_buffer = "<doStatement><keyword>" + token + "</keyword>"
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        token = str(self._tokenizer.next_token())
        if token == ".":
            temp_buffer += "<symbol>" + token + "</symbol>"
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
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
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
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
        
        # Right Hand Side Expression
        token = str(self._tokenizer.next_token())
        token = self.CompileExpression(token)
        
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
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) + "</symbol>"
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
            temp_buffer += "<symbol>" + str(self._tokenizer.next_token()) +\
                             "</symbol><expressionList>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            
            token = str(self._tokenizer.next_token())
            if token != ")":
                token = self.CompilerExpressionList(token)
            
            temp_buffer = "</expressionList><symbol>" + token + "</symbol>"
        else:
            temp_buffer = "<identifier>" + token + "</identifier>"          
                        
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
        var_modifer = str(token)
        var_type = str(self._tokenizer.next_token())

        temp_buffer = "<varDec><keyword>" + var_modifer + "</keyword>"
        if var_type in ['int', 'boolean', 'char']:
            temp_buffer += "<keyword>" + var_type + "</keyword>"
        else:
            temp_buffer += "<identifier>" + var_type + "</identifier>"
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self._tokenizer.next_token()
        
        while token == ',':
            temp_buffer = "<symbol>" + token + "</symbol>"
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"            
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
        temp_buffer = "<keyword>" + token + "</keyword>"
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = str(self._tokenizer.next_token())
        if token == ',':
            temp_buffer = "<symbol>" + token + "</symbol>"
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
            return self.CompileParamList(token)
        print token
        return token
    
    def CompileClassVarDec(self, token):
        class_var_modifer = str(token)
        class_var_type = str(self._tokenizer.next_token())

        temp_buffer = "<classVarDec><keyword>" + class_var_modifer + "</keyword>"
        if class_var_type in ['int', 'boolean', 'char']:
            temp_buffer += "<keyword>" + class_var_type + "</keyword>"
        else:
            temp_buffer += "<identifier>" + class_var_type + "</identifier>"
        temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"
        
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self._tokenizer.next_token()
        
        while token == ',':
            temp_buffer = "<symbol>" + token + "</symbol>"
            temp_buffer += "<identifier>" + str(self._tokenizer.next_token()) + "</identifier>"            
            self._out_file_object.write(temp_buffer)
            self._out_file_object.flush()
            token = str(self._tokenizer.next_token())
        
        temp_buffer = "<symbol>" + token + "</symbol></classVarDec>"
        self._out_file_object.write(temp_buffer)
        self._out_file_object.flush()
        
        token = self._tokenizer.next_token()
        
        if token in ['field', 'static']:
            return self.CompileClassVarDec(token)
        
        return token       
        