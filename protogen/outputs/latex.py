#from antlr4 import *
from protogen.ast.baseListener import baseListener
from protogen.ast.ast import *

class latex():
    def print(self,config,tree,out):
        self.config=config
        self.indent=1
        self.lineskip=-0.5
        self.tree=tree
        self.level=0
        self.line=0
        self.out=out
        self.header()
        self.block(self.tree)
        self.end()

    def header(self):
        self.out.write(
r"""
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
""")


        
    def end(self):
        self.out.write(
r"""
\end{tikzpicture}
\end{document}
""")

    def block(self,blck):
        self.out.write(r"""
        \draw[red] (%g,%g) node[anchor=west]{%s};
        """ % (self.level,self.line,blck.getName())
        )
        self.level+=self.indent
        self.line+=self.lineskip
        for i in blck.getEntries():
            if isinstance(i,block):
                self.block(i)
            if isinstance(i,field):
                self.field(i)
        self.level-=self.indent

    def field(self,field):
        self.out.write(r"""
        \draw[black] (%g,%g) node[anchor=west]{%s (%i bit) };
        """ % (self.level,self.line,field.getName(),field.getLength())        
        )
        self.line+=self.lineskip
