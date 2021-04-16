from protogen.ast.baseListener import baseListener
from protogen.ast.ast import *
from protogen.outputs.helper import canonical_name,error

class struct_c():
    def __init__(self):
        self.dtypes={8:"char",16:"short",32:"int",64:"long long"}        
        self.prefix={"uint":"unsigned","int":"signed"}
            
    def makestructs(self,config,tree,out):
        self.config=config        
        self.tree=tree
        self.out=out               
        self.block(self.tree)
        


    def block(self,blk):
        size=0
        cn=canonical_name(blk.getName())
        outs="struct __attribute__((__packed__)) "+cn+" {\n"
        align=self.config.getAlignment()
        pos=0        
        for i in blk.getEntries():
            if isinstance(i,block):
                if pos % align !=0:
                    print ("Warning: unaligned block",i.getName())
                outs+=self.block(i)                            
            if isinstance(i,field):
                outs+=self.field(i)
        outs+="};\n"
        print (outs,file=self.out)
        return "\tstruct "+cn+" "+cn+";\n"
       
    def field(self,fld):
        l=fld.getLength()
        cn=canonical_name(fld.getName())
        # we make the type:
        if fld.getType()=="BF":
            #it's a bitfield. Is the length compatible with a char array?
            if l % 8 !=0:
                error ("cannot express bitfield as array of unsigned char, length not a multiple of 8", fld.getName())
            else:
                if l //8 ==1:
                    return "\tunsigned char "+cn+";\n"                    
                else:
                    return "\tunsigned char "+cn+"["+str(l//8)+"];\n"
        if fld.type=="uint" or fld.type=="int":            
            if l not in self.dtypes:
                error("no datatype for (u)int of size",l," for field",fld.getName())
            return "\t"+self.prefix[fld.type]+" "+self.dtypes[l]+" "+cn+";\n";
            
        error ("no datatype known for field with type",fld.getType(),"for field",fld.getName())
        return ""


        
        

    
