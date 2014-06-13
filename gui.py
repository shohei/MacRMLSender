import sys
from PyQt4 import QtGui
import commands
import serial

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget,self).__init__()
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
        status,output = commands.getstatusoutput("ls /dev/tty.usb*")
        output = output.split("\n")
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("select serial port")
        if output:
            for o in output:
                self.combo.addItem(o)
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(openBtn)
        hbox1.addWidget(self.lbl)
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.combo)
        hbox2.addWidget(sendBtn)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        self.setWindowTitle("Mac RML Sender")
        self.show()
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

def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWidget()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

