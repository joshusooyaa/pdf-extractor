from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text
from pdfminer.pdftypes import resolve1

  
"""def decode_value(value):
  if isinstance(value, (PSLiteral, PSKeyword)):
    value = value.name
  
  if isinstance(value, bytes):
    value = decode_text(value)
    
  return value"""


filename = 'test2.pdf'
fp = open(filename, 'rb')

parser = PDFParser(fp)

doc = PDFDocument(parser)
catalog = resolve1(doc.catalog) # Resolve indirect object reference to ensure actual catalog object

if 'AcroForm' not in catalog:
  raise ValueError("No AcroForm Found")

fields = resolve1(catalog['AcroForm'])['Fields']

for field in fields:
  res_field = resolve1(field)
  value = res_field.get('V')
  
  if value is not None: print(value.decode('utf-8'))
