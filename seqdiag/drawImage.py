#!/bin/python

from seqdiag import parser, builder, drawer
from blockdiag.utils.bootstrap import create_fontmap
#from utils import utils


#diagram_definition = u"""
#   seqdiag {
#      browser  -> webserver [label = "GET /index.html"];
#      browser <- webserver;
#   }
#"""

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, attr):
        return self.get(attr)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__



diagram_definition =" seqdiag {"

diagram_definition += " default_fontsize = 16;\n"
diagram_definition += " node_width = 155;\n"
diagram_definition += " edge_length = 300;\n"
#Do not show activity line
diagram_definition += " activation = none;\n"
#Numbering edges automaticaly
diagram_definition += " autonumber = True;\n"



diagram_definition += "     browser  -> webserver [label = \"GET /index.html\"];"

diagram_definition += "     browser <- webserver;}"

 #set the font info
options = dict()
options['fontmap'] = ''
options['font'] = list()
options['font'].append('DejaVuSerif.ttf:1')
#options = utils.dotdict(options)
options = dotdict(options)
fm = create_fontmap(options)



tree = parser.parse_string(diagram_definition)
diagram = builder.ScreenNodeBuilder.build(tree)
#draw = drawer.DiagramDraw('PNG', diagram, filename="diagram.png")
#draw = drawer.DiagramDraw('pdf', diagram, filename="diagram.pdf")

draw = drawer.DiagramDraw('PDF', diagram, filename="diagram.pdf", debug=True, fontmap=fm)

draw.draw()
draw.save()
