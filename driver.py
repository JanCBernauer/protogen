import sys
from antlr4 import FileStream,CommonTokenStream,ParseTreeWalker

from protogen.parser.fieldsLexer import fieldsLexer
from protogen.parser.fieldsParser import fieldsParser
from protogen.ast.baseListener import baseListener
from protogen.outputs.latex import latex
from protogen.outputs.c import struct_c

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = fieldsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fieldsParser(stream)
    tree = parser.r()
    
    bl=baseListener()
    walker=ParseTreeWalker()    
    walker.walk(bl,tree)
    out=struct_c()
    out.makestructs(bl.getConfiguration(),bl.getTree(),open(argv[2],"w"))
    #out=latex()
    #out.print(bl.getConfiguration(),bl.getTree(),open(argv[2],"w"))
    

 
if __name__ == '__main__':
    main(sys.argv)
