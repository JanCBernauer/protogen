grammar fields;

r : 'protocol' NAME COMMENT? config* definition+ ;

config: alignment;

alignment: 'align' LENGTH;
tlname: 'name' NAME;

definition: field | block;

field : 'field' NAME ftype LENGTH COMMENT?;
block : 'block' NAME COMMENT? '{' definition* '}' ;

NAME : [a-zA-Z] [a-zA-Z0-9]* ;
ftype : 'BF' | 'int' | 'uint' | 'CRC';
LENGTH: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '"'[a-zA-Z0-9 ]*'"' ;


