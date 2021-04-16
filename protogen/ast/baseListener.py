from antlr4 import ParseTreeListener
from protogen.parser.fieldsParser import fieldsParser
from protogen.ast.ast import configuration,field,block

# This class defines a complete listener for a parse tree produced by fieldsParser.




class baseListener(ParseTreeListener):
    def __init__(self):
        self.config=configuration()
        self.blockstack=[]
        pass

    def getConfiguration(self):
        return self.config
    
    def getTree(self):
        return self.blockstack[0]
        
    def enterAlignment(self, ctx:fieldsParser.AlignmentContext):
        newalignment=int(ctx.LENGTH().getText())
        #print("Changing alignment from",self.config.getAlignment(),"to",newalignment)
        self.config.setAlignment(newalignment)
        pass

    def enterR(self, ctx:fieldsParser.RContext):        
        self.blockstack.append(block(ctx.NAME().getText()))        
        pass        
    
    def enterField(self, ctx:fieldsParser.FieldContext):
        fld=field(ctx.NAME().getText(),int(ctx.LENGTH().getText()),ctx.ftype().getText())        
        self.blockstack[-1].addEntry(fld)        
        pass

    

    
    def enterBlock(self, ctx:fieldsParser.BlockContext):
        blck=block(ctx.NAME().getText())
        self.blockstack[-1].addEntry(blck)
        self.blockstack.append(blck)
        pass

    
    def exitBlock(self, ctx:fieldsParser.BlockContext):
        self.blockstack.pop()
        pass


