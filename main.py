from PyQt5.QtWidgets import *
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from pdfminer.pdftypes import PDFObjRef
import json

def main():
  app = QApplication([])
  window = QWidget()
  window.setWindowTitle("PDF Cell Extractor")
  window.setGeometry(0, 0, 500, 500)
  layout = QVBoxLayout()
  
  # Widgets
  button = QPushButton("Upload PDF")
  
  # Set up events
  button.clicked.connect(on_clicked)
  
  # Add widgets to layout (layout.addWidget(feature))
  layout.addWidget(button)
  
  # set layout to window
  window.setLayout(layout)
  
  # Show layout
  window.show()
  
  # Execute
  app.exec_()


def on_clicked():
  # filenames, _ = QFileDialog.getOpenFileNames(filter="PDF Files (*.pdf)") # for future
  filename, _ = QFileDialog.getOpenFileName(filter="PDF Files (*.pdf)")
  
  json_data = data_to_json(filename)
  
  save_filename, _ = QFileDialog.getSaveFileName(filter="JSON Files (*.json)")
  
  if save_filename:
    with open(save_filename, 'w', encoding='utf-8') as json_file:
      json_file.write(json_data)
    
def data_to_json(filename):
  fp = open(filename, 'rb')

  id = 0
  data_dict = {}
  parser = PDFParser(fp)

  doc = PDFDocument(parser)
  catalog = resolve1(doc.catalog) # Resolve indirect object reference to ensure actual catalog object

  if 'AcroForm' not in catalog:
    raise ValueError("No AcroForm Found")

  fields = resolve1(catalog['AcroForm'])['Fields']
  if isinstance(fields, PDFObjRef): # Check to see if we need to resolve fields as well
    fields = resolve1(fields)

  print(type(fields))
  for field in fields:
    res_field = resolve1(field)
    value = res_field.get('V')
    
    if value is not None: data = value.decode('utf-8')
    if value == None: data = ''
      
    data_dict[id] = data
    id += 1
  
  fp.close()
  
  json_object = json.dumps(data_dict, indent=1)
  return json_object
  

if __name__ == '__main__':
  main()