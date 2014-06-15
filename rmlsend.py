#!/usr/bin/env python
#-*- coding:utf-8- *-

# Develped by Shohei Aoki, 2014

#THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
from PyQt4 import QtGui,QtCore
import commands
import serial

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.main_widget = MyWidget(self)
        self.setCentralWidget(self.main_widget)
        self.initMenu()

    def initMenu(self):
        quitAction = QtGui.QAction('&Quit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Exit application')
        self.connect(quitAction, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        aboutAction = QtGui.QAction('&About',  self)
        aboutAction.setStatusTip('About App ...')
        self.connect(aboutAction, QtCore.SIGNAL("triggered()"), self.showAbout)
        
        menuBar = self.menuBar()
        menuBar.clear()
        helpItem = menuBar.addMenu('&Help')
        helpItem.addAction(aboutAction)

#TODO: creating instance does not showing dialog
    def showAbout(self):
        d = dialogWidget(self)
        d.show()
        d.raise_()
        d.activateWindow()

#TODO : This about dialog not displaying
class dialogWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        super(dialogWidget,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About Mac RML Sender")
        label = QtGui.QLabel("About this software",self)
        self.setGeometry(200,200,200,200)
        self.show()


class MyWidget(QtGui.QWidget):
    def __init__(self,parent):
        super(MyWidget,self).__init__(parent)
        self.initUI()

    def initUI(self):
        openBtn= QtGui.QPushButton("open .rml",self)
        openBtn.clicked.connect(self.showDialog)
        self.lbl = QtGui.QLabel("Select .rml",self)
        sendBtn= QtGui.QPushButton("send",self)
        sendBtn.clicked.connect(self.sendrml)
        openFile = QtGui.QAction(QtGui.QIcon('Ghana.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        status,output = commands.getstatusoutput("ls /dev/tty.*")
        output = output.split("\n")
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("select serial port")
        if output:
            for o in output:
                self.combo.addItem(o)
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(openBtn)
        hbox1.addWidget(self.lbl)
        hbox1.addStretch(1)
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.combo)
        hbox2.addStretch(1)
        hbox2.addWidget(sendBtn)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        self.setWindowTitle("Mac RML Sender")

    def sendrml(self):
        selected_port = self.combo.currentText()
        ser = serial.Serial(port=selected_port,baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=None,xonxoff=0,rtscts=True,writeTimeout=None,dsrdtr=True)
        ser.write(self.rml)

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','~/')
        if fname:
            self.lbl.setText(fname)
        f = open(fname, 'r')
        with f:    
            data = f.read()
            self.rml = data
    def showAbout(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    w.raise_()
    w.activateWindow()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

