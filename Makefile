protogen/parser/fieldsListener.py: grammar/fields.g4
	cd grammar; antlr4  -Dlanguage=Python3 fields.g4 -o ../protogen/parser

