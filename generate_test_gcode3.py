#!/usr/bin/env python

fout = open('test.gcode','w')

for i in range(5):
    for j in range(5):
        x = 0 
        y = j*i 
        z = 10*j
        string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(i,x,y,z)
        fout.write(string)   

fout.close()
