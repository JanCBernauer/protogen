
class configuration():
    def __init__(self):
        self.alignment=8

    def getAlignment(self):
        return self.alignment

    def setAlignment(self,alignment):
        self.alignment=alignment


class entry():
    def __init__(self,name):
        self.name=name
        pass

    def getName(self):
        return self.name
    def getLength(self):
        return 0

class block(entry):
    def __init__(self,name):
        entry.__init__(self,name)    
        self.entries=[]            
        pass

    def getLength(self):
        size=0
        for f in self.entries:
            size+=f.getLength()
        return size
    
    def addEntry(self,ent):
        self.entries.append(ent)

    def getEntries(self):
        return self.entries


class field(entry):
    def __init__(self,name,length,typ):
        entry.__init__(self,name)    
        self.length=length
        self.type=typ
        pass

    def getLength(self):
        return self.length
    
    def getType(self):
        return self.type

        