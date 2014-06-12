import commands
import serial

selected_port = commands.getstatusoutput("ls /dev/tty.usb*")

ser = serial.Serial(port=selected_port,baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=None,xonxoff=0,rtscts=True,writeTimeout=None,dsrdtr=True)

fin = open("file.rml")
command = fin.read()
ser.write(command)
fin.close()

