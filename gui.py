from PyQt5.QtWidgets import *

def main():
  app = QApplication([])
  window = QWidget()
  window.setWindowTitle("ATFO Form 781 Data Extractor")
  window.setGeometry(0, 0, 500, 500)
  layout = QVBoxLayout()
  
  # Widgets
  button = QPushButton("Upload PDF")
  
  # Add widgets to layout (layout.addWidget(feature))
  layout.addWidget(button)
  
  # set layout to window
  window.setLayout(layout)
  
  # Show layout
  window.show()
  
  # Exit
  app.exec_()


if __name__ == '__main__':
  main()