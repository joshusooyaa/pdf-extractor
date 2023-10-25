from PyQt5.QtWidgets import *
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

def main():
  app = QApplication([])
  window = QWidget()
  window.setWindowTitle("ATFO Form 781 Data Extractor")
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
  
  # Exit
  app.exec_()


def on_clicked():
  filename, _ = QFileDialog.getOpenFileName(filter="PDF Files (*.pdf)")
  
  data_to_json(filename)
  # filenames, _ = QFileDialog.getOpenFileNames(filter="PDF Files (*.pdf)") # for future
  
def data_to_json(filename):
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
  
  fp.close()

if __name__ == '__main__':
  main()