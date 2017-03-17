#!/usr/bin/env python

fout = open('test.gcode','w')

for i in range(10):
    x = 10 
    y = 10
    z = 10*i
    string = "#{0} G0 X{1} Y{2} Z{3} F100\n".format(i,x,y,z)
    fout.write(string)   

fout.close()
