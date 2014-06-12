#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import commands

class Sender(QtGui.QWidget):
#class Sender(QtGui.QMainWindow):
    
    def __init__(self):
        super(Sender, self).__init__()
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("select port", self)
        self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        #self.textEdit.move(50, 350)
        self.textEdit.setGeometry(200,300,200,40)
        self.textEdit.setText("hoge")

        self.label = QtGui.QLabel(self)
        self.label.setText('Selected file')
        self.label.setWordWrap(True)
        self.label.setGeometry(10, 240, 300, 100)

        combo = QtGui.QComboBox(self)
        combo.addItem("select port") 
        status,output=commands.getstatusoutput("ls /dev/tty.*")
        output = output.split("\n")
        for o in output:
            print o
            combo.addItem(o);
        combo.move(50, 50)
        self.lbl.move(50, 150)
        combo.activated[str].connect(self.onActivated)        

        self.sizebutton = QtGui.QPushButton( "Expand", self )
        self.sizebutton.setFocusPolicy( QtCore.Qt.NoFocus )
        self.sizebutton.move( 20, 20 )
        self.connect(self.sizebutton, QtCore.SIGNAL("clicked()"), self.selectFile)
         
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Mac RML Sender')
        self.show()

    def selectFile(self):
        #QtGui.QLineEdit.setText(QtGui.QFileDialog.getOpenFileName())
        #self.sizebutton.clicked.connect(selectFile)
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.')
        print fname
        self.label.setText(fname)

        
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
                
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Sender()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

